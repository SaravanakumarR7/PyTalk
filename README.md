PyTalk:

    PyTalk is a terminal-based Python chat application that allows two users to communicate in real-time using TCP sockets. It demonstrates Python’s socket programming, threading, and asynchronous input handling with prompt_toolkit.

Installation:

    Make sure you have Python 3 installed on your system.
    
    Install the required Python package using pip:

        "pip install prompt_toolkit"


    This installs prompt_toolkit, which is used for asynchronous input/output in the terminal chat.
Features:

    Real-time messaging between server and client
    
    Threaded communication for simultaneous sending and receiving
    
    Graceful exit: type "exit" to close the connection safely
    
    Terminal-friendly interface with prompt_toolkit
    
    Handles closed connections and exceptions

Tech Stack:

    Python 3:
    
        socket module – TCP client-server communication
        
        threading – concurrent send/receive
        
        prompt_toolkit – asynchronous terminal input/output

Getting Started:

    Clone the repository:
    git clone https://github.com/your-username/PyTalk.git
    cd PyTalk
    
    Run the server: python server.py
    
    Run the client: python client.py
    (For separate machines, replace localhost with the server’s IP address in client.py)

Usage:

    Start the server
    
    Connect the client
    
    Send messages back and forth
    
    Type "exit" to terminate connection
