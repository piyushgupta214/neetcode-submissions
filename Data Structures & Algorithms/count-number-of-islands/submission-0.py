class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        island = 0

        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):

            # Boundary check
            if r < 0 or c < 0 or r >=ROW or c >= COL: 
                return
            
            # Stop if water or already visited
            if grid[r][c] == "0":
                return
            
            # Mark land as visited
            grid[r][c] = "0"
            
             # Explore all four directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # Traverse the entire grid
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    island += 1
                    dfs(r,c)
        
        return island

        