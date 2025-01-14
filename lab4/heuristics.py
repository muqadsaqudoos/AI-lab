import heapq
class PuzzleNode:
    def __init__(self, state, parent=None, move=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = 0

    def __lt__(self, other):
        # Compare nodes based on f_cost for heapq to work
        return self.f_cost < other.f_cost

    def generate_children(self):
        children = []
        row, col = None, None

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    row, col = i, j
                    break

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(r) for r in self.state]
                new_state[row][col], new_state[new_row][new_col] = (
                    new_state[new_row][new_col], new_state[row][col]
                )

                child_node = PuzzleNode(new_state, parent=self, g_cost=self.g_cost + 1)
                children.append(child_node)

        return children

    def check_index(self, value, goal_state):
        for row in range(3):
            for col in range(3):
                if goal_state[row][col] == value:
                    return row, col
        return None, None

    def calculate_heuristic(self, goal_state):
        distance = 0

        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    m, n = self.check_index(value, goal_state)
                    distance += abs(m - i) + abs(n - j)

        self.h_cost = distance
        self.f_cost = self.g_cost + self.h_cost
        return self.f_cost

class AStarSolver:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def solve(self):
        if not self.is_solvable(self.start_state):
            print("The puzzle is unsolvable.")
            return None

        priority_queue = []
        visited = set()
        start_node = PuzzleNode(self.start_state)
        start_node.calculate_heuristic(self.goal_state)
        heapq.heappush(priority_queue, (start_node.f_cost, start_node))

        while priority_queue:
            _, current_node = heapq.heappop(priority_queue)

            if current_node.state == self.goal_state:
                return self.trace_solution(current_node)

            state_tuple = tuple(tuple(row) for row in current_node.state)
            visited.add(state_tuple)

            children = current_node.generate_children()
            for child in children:
                child.calculate_heuristic(self.goal_state)
                child_state_tuple = tuple(tuple(row) for row in child.state)

                if child_state_tuple not in visited:
                    heapq.heappush(priority_queue, (child.f_cost, child))

        print("No solution exists.")
        return None

    def trace_solution(self, node):
        path = []

        while node is not None:
            path.append(node.state)
            node = node.parent

        path.reverse()
        return path

    def is_solvable(self, start_state):
        flat = [tile for row in start_state for tile in row if tile != 0]
        inversions = 0

        for i in range(len(flat)):
            for j in range(i + 1, len(flat)):
                if flat[i] > flat[j]:
                    inversions += 1

        return inversions % 2 == 0
    
    
    
def main():
    start_state = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solver = AStarSolver(start_state, goal_state)
    solution = solver.solve()

    if solution:
        print("Solution found:")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution exists.")

main()
