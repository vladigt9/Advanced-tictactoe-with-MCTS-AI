from algorithms.dia_mcts import Dia_MCTS
from algorithms.hor_mcts import Hor_MCTS
from algorithms.ver_mcts import Ver_MCTS
from algorithms.mcts import MCTS
from game.game import TicTacToe
import numpy as np

p1 = [[0,0,0,0,0],[-1,1,0,0,0],[0,0,1,-1,0],[0,-1,0,1,0],[0,0,1,0,-1]]
p2 = [[0,0,0,0,0],[0,0,1,1,0],[0,-1,1,0,0],[0,1,-1,-1,-1],[0,0,0,1,0]]
p3 = [[1,0,0,0,0],[0,1,0,0,0],[1,0,1,-1,0],[0,0,-1,0,0],[0,-1,0,0,0]]
p4 = [[0,0,0,0,1],[0,0,0,1,-1],[0,0,1,-1,-1],[0,0,0,1,-1],[0,0,0,0,0]]
p5 = [[1,1,1,0,0],[1,1,-1,0,0],[0,-1,-1,0,0],[0,0,-1,0,0],[0,0,0,0,0]]
p6 = [[0,0,0,0,0],[0,0,1,-1,0],[0,1,1,-1,0],[0,1,1,1,0],[-1,-1,-1,0,0]]
p7 = [[0,0,0,0,0],[0,0,-1,0,0],[-1,-1,1,1,1],[0,0,-1,1,0],[0,0,0,0,0]]
p8 = [[0,1,0,1,0],[0,0,1,0,0],[0,-1,-1,-1,0],[0,0,1,0,0],[0,0,0,0,0]]
p9 = [[0,0,0,0,0],[0,-1,-1,-1,0],[0,1,1,-1,0],[0,0,1,1,0],[0,0,0,0,0]]
p10 = [[0,1,-1,0,0],[0,1,-1,0,0],[0,1,-1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
p11 = [[0,0,0,0,0],[0,1,-1,1,0],[0,-1,-1,-1,0],[0,1,1,1,0],[0,0,0,0,0]]
p12 = [[0,0,0,1,1],[0,0,-1,1,0],[-1,-1,1,0,0],[-1,0,0,0,0],[0,0,0,0,0]]
p13 = [[0,0,1,1,1],[-1,1,0,0,0],[0,-1,1,0,0],[0,0,-1,1,0],[-1,-1,-1,0,0]]
p14 = [[1,1,1,0,0],[0,-1,1,0,0],[0,0,-1,1,0],[0,0,-1,-1,0],[0,0,-1,0,0]]
p15 = [[0,0,0,0,0],[0,0,1,0,0],[0,1,-1,1,0],[0,0,-1,0,0],[0,0,0,0,0]]
p16 = [[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,-1,1,-1,0],[0,1,-1,-1,0]]
p17 = [[0,1,1,0,0],[0,1,0,1,0],[0,-1,1,0,0],[0,-1,0,-1,0],[0,-1,-1,0,0]]
p18 = [[0,0,0,0,0],[0,0,1,0,0],[0,1,0,-1,0],[1,0,0,0,-1],[1,0,0,0,-1]]
p19 = [[0,0,1,0,0],[0,1,0,-1,0],[1,1,-1,-1,-1],[1,0,0,0,-1],[1,0,0,0,-1]]
p20 = [[0,0,0,0,0],[0,-1,-1,1,0],[0,-1,0,1,0],[-1,-1,1,1,1],[-1,0,0,0,1]]
positions = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]

def norm_pos(number_games=1, iterations=100):
    """
        In this function one turn is plaued from a predefined position. This is 
        done a number of times defined by the user and also the number of iterations 
        the algorithm would perform is also defined by the user. At the end the 
        specific moves completed are saved.
    """
    
    
    pos_moves = []
    
    for pos in positions:
        print(0)
        moves = {}
        
        for __ in range(number_games):
            print(__)
            game = TicTacToe(board_size=5)
            game.set_initial_state(np.array(pos))
            
            mcts = MCTS(iterations)
            move = mcts.search(game)
            
            if f'{move}' in moves:
                moves[f'{move}'] += 1
            else:
                moves[f'{move}'] = 1
        pos_moves.append(moves)
    return pos_moves

def dia_pos(number_games=1, iterations=100):
    pos_moves = []
    
    for pos in positions:
        moves = {}
        for __ in range(number_games):
            game = TicTacToe(board_size=5)
            game.set_initial_state(np.array(pos))
            
            mcts = Dia_MCTS(iterations)
            move = mcts.search(game)
            
            if f'{move}' in moves:
                moves[f'{move}'] += 1
            else:
                moves[f'{move}'] = 1
        pos_moves.append(moves)
        
    return(pos_moves)

def hor_pos(number_games=1, iterations=100):
    pos_moves = []
    
    for pos in positions:
        moves = {}
        for __ in range(number_games):
            game = TicTacToe(board_size=5)
            game.set_initial_state(np.array(pos))
            
            mcts = Hor_MCTS(iterations)
            move = mcts.search(game)
            
            if f'{move}' in moves:
                moves[f'{move}'] += 1
            else:
                moves[f'{move}'] = 1
        pos_moves.append(moves)
        
    return(pos_moves)

def ver_pos(number_games=1, iterations=100):
    pos_moves = []
    
    for pos in positions:
        moves = {}
        for __ in range(number_games):
            game = TicTacToe(board_size=5)
            game.set_initial_state(np.array(pos))
            
            mcts = Ver_MCTS(iterations)
            move = mcts.search(game)
            
            if f'{move}' in moves:
                moves[f'{move}'] += 1
            else:
                moves[f'{move}'] = 1
        pos_moves.append(moves)
        
    return(pos_moves)
