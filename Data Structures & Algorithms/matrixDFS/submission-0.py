class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return 0
        
        def dfs(i,j) -> int:
            if i < 0 or j < 0 or i >= ROWS or j>= COLS or grid[i][j] == 1 or (i,j) in seen:
                return 0
            
            if i == ROWS-1 and j == COLS-1 and grid[i][j] == 0:
                return 1

            seen.add((i,j)) 
            PATHS = 0
            PATHS += dfs(i+1, j)
            PATHS += dfs(i-1, j)
            PATHS += dfs(i, j+1)
            PATHS += dfs(i, j-1)

            seen.remove((i,j))

            return PATHS

        
        return dfs(0,0)
        