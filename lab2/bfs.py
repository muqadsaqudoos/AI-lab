from queue import deque
def bfs(edges,s,v):

    visited = [False]* v
    visited[s] = True

    queue = deque()
    queue.append(s)

    while queue:
        curr = queue.popleft()
        print(curr,end= " ")

        for i in range(len(edges[curr])):
            if visited[edges[curr][i]] == False:
                visited[edges[curr][i]] = True
                queue.append(edges[curr][i])
        

def edges(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    v = 5
    adj = [[] for _ in range(v)]

    edges(adj,0,1)
    edges(adj,0,3)
    edges(adj,1,2)
    edges(adj,2,3)
    edges(adj,3,4)
    print(adj)
    s = 0
    bfs(adj, s, v)
main()