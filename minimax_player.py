# Import libraries
from player import Player
from board import Board

# Represents a tic-tac-toe agent that evaluates moves using a minimax algorithm
class MinimaxPlayer(Player):

    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        move = None
        is_max = True

        if board.is_empty():
            move = 0
        else:
            v, move = self.get_minimax(board, is_max)
        return move

    def get_minimax(self, board: Board, is_max: bool):
        if is_max:
            return self.max_value(board)
        else:
            return self.min_value(board) 

    def max_value(self, board):
        move = None
        if self.is_terminal(board):
            return self.get_score(board), None
        else:
            v = -1000

        for a in board.get_open_spaces():
            dummy_board = board.copy()
            dummy_board.mark_space(a, self.mark)
            v2, a2 = self.min_value(dummy_board)
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(self, board):
        move = None
        if self.is_terminal(board):
            return self.get_score(board), None
        else:
            v = 1000

        for a in board.get_open_spaces():
            dummy_board = board.copy()
            dummy_board.mark_space(a, self.opponent_mark)
            v2, a2 = self.max_value(dummy_board)
            if v2 < v:
                v, move = v2, a
        return v, move

    def get_score(self, board):
        if board.has_win(self.mark):
            return 10
        elif board.has_win(self.opponent_mark):
            return -10
        else:
            return 0
        
    def is_terminal(self,board):
        if board.has_win(self.mark):
            return True
        elif board.has_win(self.opponent_mark):
            return True  
        elif board.is_full():
            return True
        return False
    