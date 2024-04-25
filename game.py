#Author: Ethan Lehutsky
#Due date: 4/21/24
#Purpose: Holds code for Game object
#Tutorial that helped me: https://www.youtube.com/watch?v=McoDjOCb2Zo

class Game:
    def __init__(self, id):
        #Bools to check if player took their turn or not
        self.p1Went = False
        self.p2Went = False
        
        #Bool for if the game is ready
        self.ready = False
        
        #Sets ID for game Instance
        self.id = id

        #Stores the moves the player can make
        self.moves = [None, None]

        #Saves player wins and ties
        self.wins = [0,0]
        self.ties = 0

    def get_player_moves(self, p):
        #p = 1 or 0 which equal to player 1 and 2 and returns the move
        return self.moves[p]
    
    #Updates moves list with the players moves
    def play(self, player, move):

        #Checks which player went and updates the p1Went and p2Went bools
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    #checks if two players are connected and if so loads game
    def connected(self):
        #tells if game is ready and updates from serverside
        return self.ready
    
    #checks if both players went
    def bothWent(self):
        return self.p1Went and self.p2Went
    
    #Tells who won the game
    def winner(self):

        #Gets the first letter of the move so I don't have to type the whole word because I am bad at speling
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        #winner Var, set to -1 in the case that their is no winner, 0 = player 1 wins, 1 = player 2 wins
        winner = -1

        #Logic to check who wins
        if p1 == 'R' and p2 == 'S':
            winner = 0
        elif p1 == 'S' and p2 == 'R':
            winner = 1
        elif p1 == 'P' and p2 == 'R':
            winner = 0
        elif p1 == 'R' and p2 == 'P':
            winner = 1
        elif p1 == 'S' and p2 == 'P':
            winner = 0
        elif p1 == 'P' and p2 == 'S':
            winner = 1
        
        #Chatgpt 3.5 made the logic easier and more condense but didn't use cause I don't like just copying and pasting GPT responses
        #winning_moves = {
            #('R', 'S'): 0,  # Rock beats Scissors
            #('S', 'R'): 1,  # Scissors beaten by Rock
            #('P', 'R'): 0,  # Paper beats Rock
            #('R', 'P'): 1,  # Rock beaten by Paper
            #('S', 'P'): 0,  # Scissors beaten by Paper
            #('P', 'S'): 1   # Paper beats Scissors
        #}

        #winner = winning_moves[(p1, p2)]

        #returns who won
        return winner
    
    #"Clears" who went
    def resetWent(self):
        self.p1Went = False
        self.p2Went = False