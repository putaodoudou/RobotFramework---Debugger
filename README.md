# Welcome to RobotFramework---Debugger

A GUI based debugger for Robot Framework tests

## Basic Idea

Debugger: React GUI, written in typescript

    - Sends commands to the listener (start, stop, pause, next, etc.)  return
    - Receives updates from the listener (variables, keywords, failures, etc.)  return
    - Updates GUI  return

Listener: Robot Framework listener, written in python

    - Starts RF Tests  return
    - Sends updates to the Debugger  return
    - Receives commands from the Debugger  return
    - Performs actions on RF tests  return

### Listener TODO

    X Create a basic listener
    - Add the ability to modify suites/tests/keywords
        - Add suite/test/keyword
        - Remove suite/test/keyword
        - Replace suite/test/keyword
    - Add the ability to filter suites/tests/keywords
        - First
        - Last
        - ByID
    - Send current suites/tests/keywords info to a socket
        - Create json compatible models for suites/tests/keywords
        - Write updated info to a socket on each event
    - Receive commands from a socket
        - Listen for POST requests without interrupting the listener
            - Use a separate thread as a server?
    - Perform commands
        - Create a json friendly commands model
        - add commands to a queue?
        - process commands on each event?

### Debugger TODO

    X Create a React App
    X Create a test suite name textbox and a start test button
    X Start a RF test/listener when the start test button is pressed
    - Ping the listener for updates on the test status
    - Send the listener commands
    - Create an actual UI
        - Create the Suite editor
        - Create the Controls (Start, Stop, Pause)

## Contributing

    - Make sure git is installed: [git it here](https://git-scm.com/)
    - Clone this repository
        - Open a shell/command prompt
        - Navigate to the directory where you would like to create the project root folder
        - Run "git clone https://github.com/FritzJay/RobotFramework---Debugger.git" without quotes
    - Change directory to the newly created folder (RobotFramework---Debugger)

That's it for now. I will update the README as a vision for the project starts to come together.

