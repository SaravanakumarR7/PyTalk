import socket
import threading
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

def receive_msg(client,session):

    while 1:
        try:
            data = client.recv(1024).decode()
            if data.lower() == "exit":
                session.app.print_text("\n Client Disconnected from the Server")
                break
            session.app.print_text(f"\n Server : {data}")
        except:
            break
    
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",5555))
print("Client Connected to Server")
session = PromptSession()
threading.Thread(target = receive_msg , args = (client,session) , daemon = True).start()

try:
    with patch_stdout():
        while 1:
            msg = session.prompt("You : ")
            if msg.lower() == "exit":
                client.sendall(msg.encode())
                print("\n Client Terminated the connection")
                break
            try:
                client.sendall(msg.encode())
            except:
                break

finally:
    client.close()

    print("\n Client Closed the Socket")
