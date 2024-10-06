def iddfs(adj, source, target , max_depth, vertices):
    for i in range(max_depth+1):
        path =  dfs(source, target, i, adj ,vertices)
        if path:
            return path

    return None 

def dfs(source, target, depth, adj,vertices):
    visited = [False]*vertices

    return rec_dfs(source, target, depth, adj,visited)

def rec_dfs(source, target, depth, adj, visited):
    if source == target:
        return [source]
    
    visited[source] = True 
    if depth== 0:
        return False
    
    for child in adj[source]:
        if visited[child] == False:

            path = rec_dfs(child,target,depth-1,adj, visited)
            if path:
                return [source] + path
        

def edges(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def main():
    vertices = 7
    adj = [[]for _ in range(vertices)]

    edges(adj,0,1)
    edges(adj,0,2)
    edges(adj,1,4)
    edges(adj,1,3)
    edges(adj,1,6)
    edges(adj,2,5)

    source = 0
    target = 5
    max_depth = 2
    
    path = iddfs(adj, source, target , max_depth, vertices)
    print(path)
main()
