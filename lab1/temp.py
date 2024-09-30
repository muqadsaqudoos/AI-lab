
def add_edge(adj, s, t):
    # Add edge from vertex s to t
    adj[s].append(t)
    # Due to undirected Graph
    adj[t].append(s)

V = 5

adj = [[] for _ in range(V)]

    # Define the edges of the graph
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
for e in edges:
    add_edge(adj, e[0], e[1])

print(adj)