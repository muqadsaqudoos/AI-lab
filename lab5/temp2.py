class Minimax:
    def __init__(self, board):
        self.board = board

    def is_terminal(self, board):
        win_conditions = [
            [board[0], board[1], board[2]],  
            [board[3], board[4], board[5]],
            [board[6], board[7], board[8]],
            [board[0], board[3], board[6]],  
            [board[1], board[4], board[7]],
            [board[2], board[5], board[8]],
            [board[0], board[4], board[8]],  
            [board[2], board[4], board[6]]
        ]
        if ['X', 'X', 'X'] in win_conditions:
            return True, 'X'
        if ['O', 'O', 'O'] in win_conditions:
            return True, 'O'
        if all(s != ' ' for s in board):
            return True, 'Draw'
        return False, None

    def utility(self, result):
        if result == 'X':
            return 1
        elif result == 'O':
            return -1
        return 0

    def minimax(self, board, depth, maximizing_player):
        terminal, result = self.is_terminal(board)
        if terminal:
            return self.utility(result)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    eval = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    eval = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self):
        best_val = float('-inf')
        best_move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                move_val = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        return best_move

initial_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
minimax = Minimax(initial_board)
best_move = minimax.best_move()
print("Best move for X:", best_move)

initial_board = [
    'X', 'O', 'X',
    ' ', 'O', ' ',
    ' ', ' ', 'O'
]
minimax = Minimax(initial_board)
best_move = minimax.best_move()
print("Best move for X:", best_move)
