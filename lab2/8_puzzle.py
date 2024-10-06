def moves(source):
    for i in range(3):
        for j in range(3):
            if source[i][j] == 0:
                row, col  = i, j
                break

    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    possible_moves= []
    for a,b in direction:
        new_row, new_col = row+a , col+b
        if new_row >=0 and new_row<3 and new_col>=0 and new_col<3:
            source_state_copy =  [row[:] for row in source]
            source_state_copy[row][col],source_state_copy[new_row][new_col]= source[new_row][new_col], source[row][col]
        
            if source_state_copy not in possible_moves:
                possible_moves.append(source_state_copy)

    return possible_moves


def iddfs(source, destination, max_depth):
    for i in range(max_depth+1):
        path = dfs(source,destination,i)
        if path:
            return path
        
    return None

def dfs(source,destiantion,depth):
    vistied = []
    return rec_dfs(source,destiantion,depth,vistied)

def rec_dfs(source,destination,depth,visited):
    if source == destination:
        return [source]
    
    if depth == 0:
        return None
    
    visited.append(source)
    
    for i in (moves(source)):
        if i not in visited:
            path = rec_dfs(i,destination,depth-1,visited)
            if path:
                return [source]+path

def main():
    source_state = [[1,2,3],[4,5,6],[7,0,8]]
    destination_state = [[1,2,3],[4,5,6],[7,8,0]]

    max_depth = 5

    path = iddfs(source_state, destination_state,max_depth)
    for i in path:
        print(i)
    print(f"In {len(path)} moves we have found the path")

main()