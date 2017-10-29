# Welcome to RobotFramework---Debugger

This is a brand new version of a Robot Framework Debugger.

## Basic Idea

Debugger: React GUI, written in typescript

    - Sends commands to the listener (start, stop, pause, next, etc.)  return
    - Receives updates from the listener (variables, keywords, failures, etc.)  return
    - Updates GUI  return

Listener: Robot Framework listener/Flask listener, written in python

    - Starts RF Tests  return
    - Sends updates to the Debugger  return
    - Receives commands from the Debugger  return
    - Performs actions on RF tests  return

### Listener TODO

    X Create a Flask Listener
    X Add a start-test-suite endpoint
    X Create a python listener
    X Disable cors
    X Initiate a robot framework test based on the test-name parameter
    - Create Models for suites, tests, keywords, ect
    - Map the suite_start and suite_end functions to inProgress boolean

### Debugger TODO

    X Create a React App
    X Create a test suite name textbox and a start test button
    X Start a RF test/listener when the start test button is pressed
    - Ping the listener for updates on the test status
