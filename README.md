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

    - <del>Create a Flask Server</del>
    - <del>Add a start-test-suite endpoint</del>
    - Initiate a robot framework test based on the test-name parameter

### Debugger TODO

    - <del>Create a React App</del>
    - <del>Create a test suite name textbox and a start test button</del>
    - Send a request to the Server when start test button is pressed
