import numpy as np

class TicTacToe:
    """
        This class implements a single instance of the game of Tic Tac Toe.
        The board size is the noly cusomizable parameter.
    
    """

    def __init__(self, board_size=4):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)
        self.current_player = 1
        
    def set_initial_state(self, state):
        """
            This method set the state of the game to a custom one define by 
            the user.
        
        """

        self.board = state
        
        p1 = 0
        p2 = 0
        for row in state:
            for square in row:
                if square == 1:
                    p1 += 1
                elif square == -1:
                    p2 += 1
                    
        if p1 > p2:
            self.current_player = -1
            

    def make_move(self, move):
        """
            This method allow for the making of a move from the current game state.
            It checks if the move is possible and then replaces the 0 value with 
            the corresponding value of the player making the move.
        
        """


        if self.board[move[0], move[1]] == 0:
            self.board[move[0], move[1]] = self.current_player
            self.current_player = -self.current_player
            return True
        return False

    
    def check_winner(self):
        """ 
            This function checks the final score of the game.
            It first go by checking rows then columns and then diagonals.
            A point is awarded when a player has made three moves in a row.
        
        """
    
    
        player_1 = 0
        player_2 = 0
        
        # check winnings on columns
        for i in range(self.board_size):
            for k in range(self.board_size-2):
                if self.board[i, k] == self.board[i, k+1] and self.board[i, k] == self.board[i, k+2]:
                    if self.board[i,k] == 1:
                        player_1+=1
                    elif self.board[i,k] == -1:
                        player_2+=1
        
        # check winnings on rows
        for i in range(self.board_size):
            for k in range(self.board_size-2):
                if self.board[k, i] == self.board[k+1, i] and self.board[k, i] == self.board[k+2, i]:
                    if self.board[k,i] == 1:
                        player_1+=1
                    elif self.board[k,i] == -1:
                        player_2+=1
        
        # check winnings on diagonals
        for i in range(self.board_size-2):
            for k in range(self.board_size-2):
                if self.board[i, k] == self.board[i+1, k+1] and self.board[i, k] == self.board[i+2, k+2]:
                    if self.board[i,k] == 1:
                        player_1+=1
                    elif self.board[i,k] == -1:
                        player_2+=1
        
        # check winnings on the other diagonals
        for i in range(2, self.board_size):
            for k in range(self.board_size-2):
                if self.board[i, k] == self.board[i-1, k+1] and self.board[i, k] == self.board[i-2, k+2]:
                    if self.board[i,k] == 1:
                        player_1+=1
                    elif self.board[i,k] == -1:
                        player_2+=1
        
        return [player_1, player_2]
    
    def is_terminal(self):
        # this method checks if the game has ended
        return np.all(self.board != 0)

    def clone(self):
        """
            This method allow to create a copy of the current state of the game
            without modifying it.
        
        """
        
        clone = TicTacToe(self.board_size)
        clone.board = np.copy(self.board)
        clone.current_player = self.current_player
        return clone

    def get_possible_moves(self):
        """
            This method returns all squares which are currently empty.
            
        """
        return [(i, j) for i in range(self.board_size) for j in range(self.board_size) if self.board[i, j] == 0]

    def print_board(self):
        """
            This prints the current state of the game to the terminal
        
        """
        for row in self.board:
            print(" ".join([str(x) if x != 0 else '.' for x in row]))
