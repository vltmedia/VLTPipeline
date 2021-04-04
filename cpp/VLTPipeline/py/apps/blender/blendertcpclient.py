import socket
import sys
import json


def CreateSocket(ip, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip, port)
    print ('connecting to '+server_address[0]+' port  '+str(server_address[1])+'')
    sock.connect(server_address)
    return sock

def SendMessageToServer(socket_, Type_, Route_, Data_, Reason_ ):
    try:

        # Send data
        message = {}
        message["Type"] = Type_
        message["Route"] = Route_
        message["Data"] = Data_
        message["Sender"] = {"Name": "Blender","Reason": Reason_}
        outmessage = json.dumps(message)
        # message = '{\n  "Type": "GET",\n  "Route": "/clients",\n  "Data": "{}",\n  "Sender": {\n    "Name": "Blender",\n    "Reason": "Init"\n  }\n}'
        # print ('sending "'+outmessage+'"')
        byt = outmessage.encode()
        socket_.sendall(byt)

        # Look for the response
        data = socket_.recv(1024).decode('utf-8')
        socket_.close()
        # print ('Received', data)
        return data


    except Exception as e:
        print (e)
        socket_.close()
        return "Failed"
 
def GetClients(socket_):
    Clients = SendMessageToServer(socket, "GET", "/clients", "{}", "Checking In on Clients")
    ClientsDict = json.loads(Clients)
    print(ClientsDict['data'])
    return ClientsDict
    
if __name__ == '__main__':
    socket = CreateSocket("localhost", 6778)
    Clients = GetClients(socket)

