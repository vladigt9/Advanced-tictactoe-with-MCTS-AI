import numpy as np
import random

class Node:
    """
        This class is created in order to store specific moves, and states of 
        the Tic Tac Toe, as well as statistics such as win rate, utc, etc.
        In addition this allow for the tree structure of the MCTS algorithm.
    
    """
    
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.visits = 0
        self.wins = 0
        self.utc = 0

    def add_child(self, child_node):
        # add a node as a child to another node
        self.children.append(child_node)

    def is_fully_expanded(self):
        # check if there are any untired moves from the current state of the game
        return 0 == len(self.get_untried_moves())

    def get_untried_moves(self):
        """"
            This method goes over all squares in the games state
            to check for possible moves. Then it gets all moves that have 
            been already tried for the current node. Last it returns the moves
            that have not yet been tried.
            
        """
        
        moves = [(i, j) for i in range(self.state.board_size) for j in range(self.state.board_size) if self.state.board[i, j] == 0]
        tried_moves = [child.move for child in self.children]
        return [move for move in moves if move not in tried_moves]

    def uct_value(self):
        """
            This method integrates the UCT formula.
            In the case that a node has note been visited a value of
            infinity is assigned in order to ensure the visit of all of them.
            Last it returns the UCT value.
        
        """
        
        if self.visits == 0:
            return float('inf')
        return (self.wins / self.visits) + np.sqrt((2 * np.log(self.parent.visits) / self.visits))
    
    def uct_child(self):
        # Returns the child with best UCT value
        return max(self.children, key=lambda child: child.uct_value())
    
    def best_win_rate(self):
        # Calculate the win rate of a node
        return self.wins / self.visits

    def best_child(self):
        # Return the node with highest win rate
        return max(self.children, key=lambda child: child.best_win_rate())


class Ver_MCTS:
    """
        This class defines the Vertical MCTS algorithm. It implements strategy 
        specific rewards.
    
    """
    
    def __init__(self, iterations=10000):
        self.iterations = iterations
        self.player = None

    def search(self, initial_state):
        """
            This method implements the MCTS algorithm.
            First it selects the player which has to make a move and the 
            initial state of the game as the root node. Then in a loop
            it goes over all steps of the MCTS algorithm (select, simulate,backpropagate)
            after which it returns the best node.
        
        """
        
        self.player = initial_state.current_player
        root = Node(state=initial_state)

        for _ in range(self.iterations):
            node = self._select(root)
            reward = self._simulate(node.state, node.move)
            self._backpropagate(node, reward)
        
        return root.best_child().move
    
    def _all_terminal_states(self, node):
        """
            This method is to check if the game has any untried states of the game,
            by recusively going through all children nodes.
        
        """
        
        if not node.is_fully_expanded():
            return True
        
        for child in node.children:
            self._all_terminal_states(child)

    def _select(self, node):
        """
            In this method the select part of MCTS is performed.
            It is performed only if the game has not reached a terminal state.
            Then it is checked if all possible moves have been explored and 
            if yes then it explore the child with highest UCT else it performs 
            any of the moves that have not been tried yet.
        
        """
        
        while not node.state.is_terminal():
            
            if node.is_fully_expanded():
                node = node.uct_child()
            else:
                return self._expand(node)
        
        return node

    def _expand(self, node):
        """
            In this method the expansion step of MCTS is performed.
            First the current game state is cloned and at random a untried 
            move is performed. Then this new state is saved as a child node 
            and added to the parent.
        
        """
        
        untried_moves = node.get_untried_moves()
        new_state = node.state.clone()
        move = random.choice(untried_moves)
        new_state.make_move(move)
        child_node = Node(state=new_state, parent=node, move=move)
        node.add_child(child_node)
        return child_node

    def _simulate(self, state, move):
        """
            In this method the simulation part of MCTS is performed.
            First the current state is cloned, then at random moves are 
            performed until the game ends. Then the winner is found and 
            the appropriate rewards are returned. In this the diagonal strategy 
            rewards are implemented.
        
        """
        
        cloned_state = state.clone()
        while not cloned_state.is_terminal():
            possible_moves = [(i, j) for i in range(cloned_state.board_size) for j in range(cloned_state.board_size) if cloned_state.board[i, j] == 0]
            move = random.choice(possible_moves)
            cloned_state.make_move(move)
        winner = cloned_state.check_winner()
        
        if winner[0] > winner[1]:
            
            if self.player == 1:
                if move[0] != state.board_size-1 and state.board[move[0]+1, move[1]] == 1:
                    return 1.5
                elif move[0] != 0 and state.board[move[0]-1, move[1]] == 1:
                    return 1.5
                else:
                    return 1
            else:
                return -1
            
        elif winner[0] < winner[1]:
            
            if self.player == -1:
                if move[0] != state.board_size-1 and state.board[move[0]+1, move[1]] == -1:
                    return 1.5
                elif move[0] != 0 and state.board[move[0]-1, move[1]] == -1:
                    return 1.5
                else:
                    return 1
            else:
                return -1
            
        else:
            if move[0] != state.board_size-1 and state.board[move[0]+1, move[1]] == self.player:
                return 0.5
            elif move[0] != 0 and state.board[move[0]-1, move[1]] == self.player:
                return 0.5
            else:
                return 0

    def _backpropagate(self, node, reward):
        """
            This method implements the last part of the MCTS algorithm. In it 
            the rewards obtained from the simulations are used to update the 
            statistics of the branches.
        
        """
        
        while node is not None:
            node.visits += 1
            node.wins += reward
            node = node.parent
