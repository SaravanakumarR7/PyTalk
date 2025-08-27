import socket
import threading
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

def receive_msg(client,session):

    while 1:
        try:
            data = client.recv(1024).decode()
            if data.lower() == "exit":
                print("\n Client Disconnected from the Server")
                break
            print("\n Client : ", data)
        except:
            break

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",5555))
server.listen(1)
print("Server Listening....")
client,addr = server.accept()
print(f"Client Connected from {addr}")
session = PromptSession()
threading.Thread(target = receive_msg , args = (client,session) , daemon = True).start()

try:
    with patch_stdout():
        while 1:
            msg = session.prompt("You : ")
            if msg.lower() == "exit":
                print("\n Server Terminated the Connection")
                break
            try:
                client.sendall(msg.encode())
            except:
                break
finally:
    client.close()
    print("Client Socket Closed")
    server.close()
    print("Server Socket Closed")