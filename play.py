import tkinter as tk
from tkinter import messagebox
from algorithms.mcts import MCTS
from game.game import TicTacToe

"""
File that introduces a GUI for the game.
The game can be started by simply runing the file.
In order to change the board size go to the bottom of the file.
"""

class TicTacToeGUI:
    def __init__(self, board_size=4):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("608x483")
        self.root.resizable(False, False)
        self.root.configure(bg="#12263A")
        self._show_menu()
        self.board_size = board_size
        self.player = 1
        self.difficulty = None
        self.game_mode = None
        
    def _show_menu(self):
        """
            Starting menu of the game where one can choose 
            the mode - vs player or vs AI
        """
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        title = tk.Label(self.root, text="Welcome to Tic Tac Toe", font=("Arial", 24), bg="#12263A", fg="white")
        title.pack(pady=20)

        button_vs_ai = tk.Button(self.root, text="vs Player", font=("Arial", 18), bg="#F4D1AE", fg="black", command=lambda: self._set_mode(1))
        button_vs_ai.pack(pady=10)
        button_vs_ai = tk.Button(self.root, text="vs AI", font=("Arial", 18), bg="#F4D1AE", fg="black", command=lambda: self._set_mode(2))
        button_vs_ai.pack(pady=10)

                
    def _set_mode(self, mode):
        """
            Function to redirect to based on game mode selected.
        """
        
        self.game_mode = mode
        
        if mode == 1:
            self._start_player_game()    
        else:
            self._choose_difficulty()
        
    def _choose_difficulty(self):
        """
            Menu to select wath difficulty to play against.
        """
        
        for widget in self.root.winfo_children():
            widget.destroy()
            
        title = tk.Label(self.root, text="Choose Difficulty", font=("Arial", 24), bg="#12263A", fg="white")
        title.pack(pady=20)

        tk.Button(self.root, text="1", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_difficulty(1)).pack(pady=10)
        tk.Button(self.root, text="2", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_difficulty(2)).pack(pady=10)
        tk.Button(self.root, text="3", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_difficulty(3)).pack(pady=10)
        tk.Button(self.root, text="4", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_difficulty(4)).pack(pady=10)
        tk.Button(self.root, text="5", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_difficulty(5)).pack(pady=10)
        
    def _set_difficulty(self, level):
        """
            Funtion to set the specific diffuclty of the game.
        """
        
        self.difficulty = level*750
        self._choose_player()
        
    def _choose_player(self):
        """
            When playing against the AI, a menu to chose wether to start first 
            or second.
        """
        
        
        for widget in self.root.winfo_children():
            widget.destroy()
            
        title = tk.Label(self.root, text="Choose Player", font=("Arial", 24), bg="#12263A", fg="white")
        title.pack(pady=20)

        tk.Button(self.root, text="X", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_player(1)).pack(pady=10)
        tk.Button(self.root, text="O", font=("Arial", 18), bg="#F4D1AE", command=lambda: self._set_player(-1)).pack(pady=10)
        
    def _set_player(self, player):
        """
            A function to set which player the user is going to be.
        """
        
        
        self.player = player
        self._start_ai_game()
            
    def _start_player_game(self):
        """
            Start a game of player vs player
        """
        
        
        for widget in self.root.winfo_children():
            widget.destroy()

        self.game = TicTacToe(self.board_size)
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(
                    self.root, text='', font=("Arial", 20, "bold"), width=6, height=3,
                    bg="#F4D1AE", fg="#000",
                    command=lambda row=i, col=j: self._on_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button
        
    def _start_ai_game(self):
        """
            Starts a game of player vs AI.
        """
        
        for widget in self.root.winfo_children():
            widget.destroy()

        self.game = TicTacToe(self.board_size)

        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                button = tk.Button(
                    self.root, text='', font=("Arial", 20, "bold"), width=6, height=3,
                    bg="#F4D1AE", fg="#000",
                    command=lambda row=i, col=j: self._on_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button
        
        if self.player == -1:
            self._ai_make_move()
        
    def _on_click(self, row, col):
        """
            A function to control the actions on a square click.
        """
        
        if self.game.current_player == self.player and self.game.make_move((row, col)):
            self._update_board_display(row, col, 'X' if self.player == 1 else "O")
        
            if self.game.make_move((row, col)):
                self.buttons[row][col]["text"] = 'X' if self.game.current_player == -1 else 'O'
            
            if self.game_mode == 2:
                self._check_game_end()
                self._ai_make_move()
            else:
                self.player *= -1
                self._check_game_end()
            
    
    def _ai_make_move(self):
        """
            A function to control the AI moves.
        """
        
        mcts = MCTS(self.difficulty)
        move = mcts.search(self.game)
        self.game.make_move(move)
        self._update_board_display(move[0], move[1], 'X' if self.player == -1 else 'O')
        self._check_game_end()
    
    def _update_board_display(self, row, col, player_symbol):
        """
            Update button after selection
        """
        
        self.buttons[row][col]["text"] = player_symbol
        self.buttons[row][col]["state"] = "disabled"
        
    def _check_game_end(self):
        """
            Check if game has ended.
        """
        
        if not self.game.is_terminal():
            return
        
        winner = self.game.check_winner()
        if sum(winner) > 0:
            self._end_game(winner)
        elif self.game.is_terminal():
            messagebox.showinfo("Game Over", "It's a tie!")
            self._reset_game()
        else:
            self.label["text"] = "Player X's turn" if self.game.current_player == 1 else "Player O's turn"
    
    def _end_game(self, winner):
        """
            Display a message which player has won and by how much.
        """
        
        
        if winner[0] > winner[1]:
            messagebox.showinfo("Game Over", f'Player X wins! Score: {winner[0]}:{winner[1]}')
        elif winner[1] > winner[0]:
            messagebox.showinfo("Game Over", f"Player O wins! Score: {winner[0]}:{winner[1]}")
        else:
            messagebox.showinfo("Game Over", f"It's a draw.")
        self._reset_game()
    
    def _reset_game(self):
        """
            Resets the game and gets the player to the start menu.
        """
        
        self._show_menu()
        self.difficulty = None
        self.game_mode = None
        self.player = 1
    
    def start(self):
        """
            Starts the game
        """
        
        self.root.mainloop()

if __name__ == "__main__":
    app = TicTacToeGUI(board_size=4)
    app.start()
