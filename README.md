# CS 350 Portfolio Submission  

This repository contains my portfolio artifacts for CS 350: Emerging Systems Architectures and Technologies. The projects in this course focused on writing interface software to control hardware components, analyzing hardware architecture design, and combining different technologies into working embedded systems. The two artifacts I selected show my ability to work with UART communication to control hardware and to integrate sensors with an LCD display.  

# Portfolio Reflection

## Summary of the Projects  
For Milestone 2, I created a Python program that used UART communication to send commands from a client to a Raspberry Pi. The Raspberry Pi would read these commands and control an LED, responding to simple instructions like ON, OFF, EXIT, and QUIT. This project was all about building an interface that could react in real time to outside input while keeping the communication reliable. For Module 6, I worked on integrating a temperature and humidity sensor with a 16x2 LCD display. The program displayed live sensor readings and let me switch between Celsius and Fahrenheit, while also keeping the text formatted clearly on the small screen.  

## What I Did Well  
I feel I did a good job making sure the code was solid and handled errors properly. In Milestone 2, I made sure unknown commands did not crash the program and used error handling so the program could shut down cleanly without leaving the GPIO pins in the wrong state. In Module 6, I focused on making the display readable by shortening labels and rounding values so everything fit neatly on the screen.  

## Where I Could Improve  
One thing I could improve is doing more planning before I start coding. A lot of times I fixed issues as they came up instead of anticipating them ahead of time. For example, the LCD flickering problem could have been avoided if I had thought more about refresh timing before I started.  

## Tools and Resources Added to My Support Network  
Working on these projects gave me practice with the Raspberry Pi GPIO library, UART serial communication, and QWIIC sensors. I also learned how valuable it is to use lab guides and tutorials as a foundation, while going to the official Python and Raspberry Pi documentation when I needed more detail.  

## Transferable Skills  
The most important skills I am taking away from this are debugging hardware and software together, understanding communication protocols like UART, and writing code that is clean and easy to follow. These are skills I can apply in future embedded projects, IoT development, and other courses that mix hardware with software.  

## Making the Projects Maintainable, Readable, and Adaptable  
I kept the code easy to maintain by writing it in a clear and modular way and by avoiding unnecessary clutter. I also made sure the GPIO pins always reset at the end of the program so they would not interfere with other work later on. For Module 6, the LCD logic is easy to change, so it could be adapted to show other types of sensor data besides temperature and humidity.  
