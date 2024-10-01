def dfs(edges,s,v):
    visited = [False]*v
    rec_dfs(visited,edges,s)

def rec_dfs(visited, edges, s):
    visited[s] = True
    print(s,end= " ")
    for i in range(len(edges[s])):
        if visited[edges[s][i]] == False:
            rec_dfs(visited, edges, edges[s][i])

def edges(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    v = 7
    adj = [[] for _ in range(v)]

    edges(adj,0,1)
    edges(adj,0,2)
    edges(adj,1,4)
    edges(adj,1,3)
    edges(adj,1,6)
    edges(adj,2,5)
    s = 0
    dfs(adj, s, v)
main()