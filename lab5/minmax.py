class Minimax:
    def __init__(self, game_state):
        self.game_state = game_state

    def is_terminal(self, state):
        win_conditions = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[0][2], state[1][1], state[2][0]]
        ]

        for win in win_conditions:
            if win == ['X', 'X', 'X']:
                return True, 'X'
            elif win == ['O', 'O', 'O']:
                return True, 'O'

        if all(j != " " for row in state for j in row):
            return True, 'Draw'

        return False, None

    def utility(self, state):
        terminal, result = self.is_terminal(state)
        if terminal:
            if result == 'X':
                return 1
            elif result == 'O':
                return -1
            else:
                return 0
        return None

    def minimax(self, state, depth, maximizing_player):
        terminal, result = self.is_terminal(state)
        if terminal:
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_available_moves(state):
                new_state = self.make_move(state, move, 'X')
                eval = self.minimax(new_state, depth + 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_available_moves(state):
                new_state = self.make_move(state, move, 'O')
                eval = self.minimax(new_state, depth + 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, state):
        best_value = float('-inf')
        best_move = None

        for move in self.get_available_moves(state):
            new_state = self.make_move(state, move, 'X')
            move_value = self.minimax(new_state, 0, False)

            if move_value > best_value:
                best_value = move_value
                best_move = move

        return best_move

    def get_available_moves(self, state):
        available_moves = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == " ":
                    available_moves.append((i, j))
        return available_moves

    def make_move(self, state, move, player):
        new_state = [row[:] for row in state]
        new_state[move[0]][move[1]] = player
        return new_state

def main():
    game_state = [
        ['X', 'O', '  '],
        ['O', 'X', ' '],
        [' ', ' ', ' ']
    ]

    a = Minimax(game_state)
    best_move = a.best_move(game_state)
    print(best_move)

main()
