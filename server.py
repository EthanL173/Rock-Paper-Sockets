import socket
from _thread import *
import pickle 
from game import Game

#Stores ips of connected clients
connected = set()
#Stores Games- id and game object
games = {}
#Keeps track of games and ensures none are overwritten
idCount = 0



#saved info to save time getting it back
#10.175.34.2
#5555
server =  input('Enter IP: ')
#ensuring that the user puts in numbers for port
try:
    port =  int(input('Enter port: '))
except:
    print('Port number should be a number') 

#connecting to socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    sock.bind((server, port))
except:
    print('Socket Failed to Bind')

try:
    sock.listen(2)
    print('Waiting for connection, Server Runinng')
except:
    print('invaild IP address')





def thread_client (con, p, gameId):
    #Keep track of players if one disconnects for example
    global idCount
    #Sends data to let client know if player 1 or 2
    con.send(str.encode(str(p)))

    reply = ''
    while True:
        try:
            data = con.recv(4096).decode()

            #Checks to see if game still exist
            if gameId in games:
                game = games[gameId]

                #data is empty stop connection 
                if not data:
                    break
                else:
                    #checking to see if game needs reseting
                    if data == 'reset':
                        game.resetWent()
                    #Checks if it recived a move
                    elif data != 'get':
                        game.play(p, data)


                    #Send game data to client
                    reply = game
                    con.sendall(pickle.dumps(reply))
            else:
                print('Error')
                break
        except:
            print('Error')
            break
    #If a player disconnects it will the delete the game to save space
    print('No Connection')
    try:
        del games[gameId]
        print('Game Closed')
    except:
        print('Game already deleted')
        pass
    idCount -= 1
    con.close()

# def close():
#     con.shutdown(socket.SHUT_RDWR)
#     con.close()
#     print('Shutting down....')




run = True
while run:
    try:
        con, addr = sock.accept()
        print('Connection established to: ' , addr)

        idCount += 1

        #current player
        p = 0

        #Keeps track of what id game is gonna be
        gameId = (idCount - 1)//2

        #checks if new game needs to be made
        if idCount % 2 == 1:
            #adds new game id
            games[gameId] = Game(gameId)
            print('Creating new game......')
        else:
            #Do not need to make a new game
            #Game ready to play because two people are connected
            games[gameId].ready = True
            p = 1


        start_new_thread(thread_client, (con, p, gameId))
    except:
        run = False
        print('Failed to establish connection try again')



