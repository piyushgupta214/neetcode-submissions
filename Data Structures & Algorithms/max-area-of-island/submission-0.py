class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        


        ROWS = len(grid)
        COLS = len(grid[0])
        islands = [0]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visit = set()

        def bfs(r,c):
            visit.add((r, c))
            queue = deque()
            queue.append((r,c))
            while queue:
                (row, col) = queue.popleft()
                for (dr,dc) in directions:
                    newRow = row+dr
                    newCol = col+dc

                    if newRow < 0 or newCol < 0 or newRow >= ROWS or newCol >= COLS or (newRow, newCol) in visit or grid[newRow][newCol] == 0:
                        continue
                    queue.append((newRow, newCol))
                    visit.add((newRow, newCol))




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    visit.add((r,c))
                    bfs(r,c)
                    islands.append(len(visit))
        
        maxArea = 0

        for i in range(1, len(islands)):
            area = islands[i] - islands[i - 1]
            maxArea = max(maxArea, area)

        return maxArea
        