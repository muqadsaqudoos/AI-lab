class AlphaBetaProuning:
    def __init__(self, game_state, max_depth=float('inf'), ab_pruning=True):
        self.game_state = game_state
        self.max_depth = max_depth
        self.ab_pruning = ab_pruning
        self.nodes = 0

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
        return 0  
    
    def alphaBeta(self, state, depth, alpha, beta, maximizing_player):
        self.nodes += 1  
        terminal, result = self.is_terminal(state)
        if terminal or depth == self.max_depth:
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for move in self.get_available_moves(state):
                new_state = self.make_move(state, move, 'X')
                eval = self.alphaBeta(new_state, depth + 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                if self.ab_pruning:
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.get_available_moves(state):
                new_state = self.make_move(state, move, 'O')
                eval = self.alphaBeta(new_state, depth + 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                if self.ab_pruning:
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  
            return min_eval

    def best_move(self, state):
        self.nodes = 0  
        best_value = float('-inf')
        best_move = None

        for move in self.get_available_moves(state):
            new_state = self.make_move(state, move, 'X')
            move_value = self.alphaBeta(new_state, 0, float('-inf'), float('inf'), False)

            if move_value > best_value:
                best_value = move_value
                best_move = move

        print(f"Best move: {best_move}, Nodes evaluated for this move: {self.nodes}")
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

    def play_game(self):
        state = [row[:] for row in self.game_state]
        player_turn = 'O'
        
        total_nodes = 0  
        while True:
            print("\ncurrent board:")
            for row in state:
                print(row)
            
            if player_turn == 'O':  
                move = tuple(map(int, input("My move: ").split()))
                state = self.make_move(state, move, 'O')
            else: 
                move = self.best_move(state)
                state = self.make_move(state, move, 'X')
                total_nodes += self.nodes
                print(f"AI ({player_turn}) moves to {move}")

            terminal, winner = self.is_terminal(state)
            if terminal:
                print("\nFinal board:")
                for row in state:
                    print(row)
                if winner == 'Draw':
                    print("Draw!")
                else:
                    print(f"{winner} wins!")
                break
            
            player_turn = 'O' if player_turn == 'X' else 'X'

        print(f"Total nodes evaluated in game: {total_nodes}")
        return total_nodes


def main():
    game_state = [
    ['O', 'X', ' '],
    [' X', 'O', ' '],
    [' ', ' ', 'O']
]
    
    print("playing with AlphaBeta pruning:")
    with_pruning = AlphaBetaProuning(game_state, max_depth=3, ab_pruning=True)
    nodes_with_pruning = with_pruning.play_game()

    print("\nplaying without AlphaBeta pruning:")
    without_pruning = AlphaBetaProuning(game_state, max_depth=3, ab_pruning=False)
    nodes_without_pruning = without_pruning.play_game()

    print("\nComparison: ")
    print(f"with Alpha-Beta pruning: {nodes_with_pruning} ")
    print(f"without Alpha-Beta pruning: {nodes_without_pruning} ")

main()
