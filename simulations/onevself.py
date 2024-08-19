from algorithms.dia_mcts import Dia_MCTS
from algorithms.hor_mcts import Hor_MCTS
from algorithms.ver_mcts import Ver_MCTS
from algorithms.mcts import MCTS
from game.game import TicTacToe

def D_D(number_games=1, iterations=100):
    """
        In this function the a specific match-up is simulated. This is done 
        for a number of times defined by the user and the iterations performed 
        by the algorithm is also defined by the user.
        
    """
    
    first = 0
    second = 0
    draw = 0
    
    for _ in range(number_games):
        
        game = TicTacToe(board_size=5)
        
        while game.is_terminal() == False:
            
            mcts = Dia_MCTS(iterations)
            move = mcts.search(game)
            game.make_move(move)
            
        winner = game.check_winner()
        if winner[0] > winner[1]:
            first+=1
        elif winner[0] < winner[1]:
            second+=1
        else:
            draw+=1

    return [first,second,draw]

def V_V(number_games=1, iterations=100):
    first = 0
    second = 0
    draw = 0
    
    for _ in range(number_games):
        
        game = TicTacToe(board_size=5)
        
        while game.is_terminal() == False:
            
            mcts = Ver_MCTS(iterations)
            move = mcts.search(game)
            game.make_move(move)
            
        winner = game.check_winner()
        if winner[0] > winner[1]:
            first+=1
        elif winner[0] < winner[1]:
            second+=1
        else:
            draw+=1

    return [first,second,draw]

def H_H(number_games=1, iterations=100):
    first = 0
    second = 0
    draw = 0
    
    for _ in range(number_games):
        
        game = TicTacToe(board_size=5)
        
        while game.is_terminal() == False:
            
            mcts = Hor_MCTS(iterations)
            move = mcts.search(game)
            game.make_move(move)
            
        winner = game.check_winner()
        if winner[0] > winner[1]:
            first+=1
        elif winner[0] < winner[1]:
            second+=1
        else:
            draw+=1

    return [first,second,draw]

def N_N(number_games=1, iterations=100):
    first = 0
    second = 0
    draw = 0
    
    for _ in range(number_games):
        
        game = TicTacToe(board_size=5)
        
        while game.is_terminal() == False:
            
            mcts = MCTS(iterations)
            move = mcts.search(game)
            game.make_move(move)
            
        winner = game.check_winner()
        if winner[0] > winner[1]:
            first+=1
        elif winner[0] < winner[1]:
            second+=1
        else:
            draw+=1

    return [first,second,draw]
