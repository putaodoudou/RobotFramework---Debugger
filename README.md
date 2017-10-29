# Welcome to RobotFramework---Debugger

This is a brand new version of a Robot Framework Debugger.

## Basic Idea

Debugger: React GUI, written in typescript

    - Sends commands to the listener (start, stop, pause, next, etc.)  return
    - Receives updates from the listener (variables, keywords, failures, etc.)  return
    - Updates GUI  return

Server: Robot Framework listener/Flask server, written in python

    - Starts RF Tests  return
    - Sends updates to the Debugger  return
    - Receives commands from the Debugger  return
    - Performs actions on RF tests  return

### Server TODO

    X Create a Flask Server
    X Add a start-test-suite endpoint
    X Create a python listener/server
    X Disable cors
    - Initiate a robot framework test based on the test-name parameter

### Debugger TODO

    X Create a React App
    X Create a test suite name textbox and a start test button
    - Start a RF test/listener when the start test button is pressed
