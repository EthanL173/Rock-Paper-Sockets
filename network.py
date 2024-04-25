#Author: Ethan Lehutsky
#Due date: 4/21/24
#Purpose: File that holds the logic for  the network object and helps the client connect to the .
#Tutorial that helped me: https://www.youtube.com/watch?v=McoDjOCb2Zo

import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = input('Enter Host Server IP: ')
        try:
            self.port =  int(input('Enter Host Port: '))
        except:
            print('Invalid Port Click game and try again')
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    #connect to server
    def connect(self):
        try:
            self.client.connect(self.addr)
            #returns player number
            return self.client.recv(2048).decode()
        except:
            print('oops')
    
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except:
           print('error')