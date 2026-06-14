INF = 2147483647
from collections import deque

def WallsAndGates(grid):
    if not grid or not grid[0]:
        return
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ROWS, COLS = len(grid), len(grid[0])
    
    queue = deque()
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                queue.append((r, c))
    
    distance = 0
    while queue:
        distance += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            row, col = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if (0 <= new_row < ROWS) and (0 <= new_col < COLS) and grid[new_row][new_col] == INF:
                        grid[new_row][new_col] = distance
                        queue.append((new_row, new_col))
    return grid
            

grid = [
    [INF, -1, 0,  INF],
    [INF, INF, INF,  -1],
    [INF,  -1,  INF,  -1],
    [0, -1, INF, INF],
]

print(WallsAndGates(grid))


    
        
    