import heapq

class Node:
    def __init__(self, state, parent, move, h_cost):
        self.state = state  
        self.parent = parent
        self.move = move
        self.h_cost = h_cost  

    def __lt__(self, other):
        return self.h_cost < other.h_cost
    
    def generate_children(self, goal):
        children = []
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        for move in moves:
            new_pos = (self.state[0] + move[0], self.state[1] + move[1])
            if 0 <= new_pos[0] < 5 and 0 <= new_pos[1] < 5:  
                h_cost = abs(new_pos[0] - goal[0]) + abs(new_pos[1] - goal[1])
                children.append(Node(new_pos, self, move, h_cost))
        return children

class GreedyBestFirstSearch:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.open_list = []
        self.closed_list = set()

    def solve(self):
        start_node = Node(self.start, None, None, 0)
        heapq.heappush(self.open_list, (0, start_node))

        while self.open_list:
            _, current_node = heapq.heappop(self.open_list)

            if current_node.state == self.goal:
                return self.trace_solution(current_node)

            self.closed_list.add(current_node.state)

            for child in current_node.generate_children(self.goal):
                if child.state not in self.closed_list:
                    heapq.heappush(self.open_list, (child.h_cost, child))

    def trace_solution(self, node):
        path = []
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]

gbfs = GreedyBestFirstSearch((0, 0), (4, 4))
solution = gbfs.solve()
print("Path:", solution)
