class PuzzleNode:
    def _init_(self, state, parent, move, g_cost, h_cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost

    def generate_children(self): 
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    row, col  = i, j
                    break

            direction = [[-1,0],[1,0],[0,-1],[0,1]]
            possible_moves= []
            for a,b in direction:
                new_row, new_col = row+a , col+b
                if new_row >=0 and new_row<3 and new_col>=0 and new_col<3:
                    source_state_copy =  [row[:] for row in self.state]
                    source_state_copy[row][col],source_state_copy[new_row][new_col]= self.state[new_row][new_col], self.state[row][col]
                
                    if source_state_copy not in possible_moves:
                        possible_moves.append(source_state_copy)

            return possible_moves# Generate possible child nodes by moving the empty tile pass
    def calculate_heuristic(self, goal_state):
        self.h_cost = 0
        for i in self.state:
            for j in self.state:
                if self.state[i][j] != goal_state[i][j]:
                    self.h_cost += 1
        pass # Calculate heuristic based on the current state and goal pass
class AStarSolver: 
    def _init_(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
         # Initialize the A* solver with start and goal states pass
    def solve(self): 
        pass# Implement the A* algorithm to solve the puzzle pass
    def trace_solution(self, node): 
        pass# Trace back from the goal to get the solution path pass
    def is_solvable(self, state):
        pass # Check if the puzzle state is solvable Pass


