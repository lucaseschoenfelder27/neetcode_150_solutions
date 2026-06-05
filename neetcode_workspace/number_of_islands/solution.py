class Solution:
    # Time: O(?)
    # Space: O(?)
    def num_islands(self, grid: list[list[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # check bounds
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return
            
            grid[r][c] = "0"
            for dr, dc in directions:
                #print('dr, dc: ', dr, dc)
                dfs(r + dr, c + dc)
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands

