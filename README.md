# Welcome to RobotFramework---Debugger

This is a brand new version of a Robot Framework Debugger.

## Basic Idea


Debugger: React GUI, written in typescript

    - Start's python listener

    - Sends commands (start, stop, pause, next, etc.)

    - Receives updates (variables, keywords, failures, etc.)

    - Updates GUI


Server: Robot Framework listener/SimpleHTTPServer, written in python

    - Starts RF Tests

    - Sends updates to Debugger

    - Receives commands from Debugger
    
    - Performs actions on RF tests
