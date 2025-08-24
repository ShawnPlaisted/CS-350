import RPi.GPIO as GPIO
import time
import threading
from statemachine import StateMachine, State
import I2C_LCD_driver
RED_LED = 18
BLUE_LED = 23
BUTTON = 24
DOT_DURATION = 0.5
DASH_DURATION = 1.5
SYMBOL_PAUSE = 0.25
LETTER_PAUSE = 0.75
WORD_PAUSE = 3.0
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': ' '
}
MESSAGES = ["HELLO WORLD", "SOS"]
current_msg_index = 0
message_lock = threading.Lock()
stop_thread = False
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
lcd = I2C_LCD_driver.lcd()
def blink_led(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)
class MorseStateMachine(StateMachine):
    idle = State('Idle', initial=True)
    dot = State('Dot')
    dash = State('Dash')
    pause = State('Pause')
    letter_pause = State('Letter Pause')
    word_pause = State('Word Pause')
    to_dot = idle.to(dot)
    to_dash = idle.to(dash)
    to_pause = dot.to(pause) | dash.to(pause)
    to_letter_pause = pause.to(letter_pause)
    to_word_pause = pause.to(word_pause)
    to_idle = pause.to(idle) | letter_pause.to(idle) | word_pause.to(idle)
machine = MorseStateMachine()
def morse_thread():
    global current_msg_index, stop_thread
    while not stop_thread:
        message_lock.acquire()
        message = MESSAGES[current_msg_index]
        message_lock.release()
        lcd.lcd_display_string(f"Message: {message}", 1)
        for char in message:
            morse = MORSE_CODE_DICT.get(char.upper(), '')
            for symbol in morse:
                if symbol == '.':
                    machine.to_dot()
                    blink_led(RED_LED, DOT_DURATION)
                elif symbol == '-':
                    machine.to_dash()
                    blink_led(BLUE_LED, DASH_DURATION)
                machine.to_pause()
                time.sleep(SYMBOL_PAUSE)
            if char == ' ':
                machine.to_word_pause()
                time.sleep(WORD_PAUSE)
            else:
                machine.to_letter_pause()
                time.sleep(LETTER_PAUSE)
            machine.to_idle()
def button_callback(channel):
    global current_msg_index
    with message_lock:
        current_msg_index = (current_msg_index + 1) % len(MESSAGES)
    lcd.lcd_display_string("Switching msg...", 2)
    time.sleep(1)
    lcd.lcd_display_string(" " * 16, 2)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=button_callback, bouncetime=300)
t = threading.Thread(target=morse_thread)
t.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_thread = True
    t.join()
    GPIO.cleanup()
    lcd.lcd_display_string("System halted", 1)
    time.sleep(2)
    lcd.lcd_clear()
