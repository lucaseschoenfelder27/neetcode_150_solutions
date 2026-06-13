class Solution:
    # Time: O(?)
    # Space: O(?)
    def oranges_rotting(self, grid: list[list[int]]) -> int:
        def has_fresh():
            return any(1 in row for row in grid)
        
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        t = 0
        
        changed = True
        while has_fresh() and changed:
            changed = False
            
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 2:
                        
                        for dr, dc in directions:
                            r, c = row + dr, col + dc
                            
                            if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1:
                                grid[r][c] = 3
                                changed = True
            
            if not changed:
                return -1
            
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 3:
                        grid[row][col] = 2
            
            t += 1
        
        return t if not has_fresh() else -1
