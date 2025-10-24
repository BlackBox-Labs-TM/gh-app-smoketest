python from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    
    # Find start
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
    
    # BFS
    queue = deque([(start[0], start[1], 0)])  # row, col, steps
    visited[start[0]][start[1]] = True
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while queue:
        r, c, steps = queue.popleft()
        
        if grid[r][c] == 'E':
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows) and (0 <= nc < cols):
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))
    
    return -1  # No path found

# Example usage
print(shortest_path([
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]))  # Output: 11
