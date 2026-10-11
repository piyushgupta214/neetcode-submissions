class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # so  first find rotten orange in the grid which could be anywhere 
        # once we have that rotten orange we add that into our queue 
        # this is min 0 
        # now we loop until the queue is empty
        # we pop an item and  
        # and check his horizontal and vertical neighbour 
        # if they are fresh fruits we add those fresh fruits to the queue and that becomes next min and we can set their value to 2 
        # and keep going until 

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        minutes = 0
        fresh = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        # find all rotten oranges in the grid at minutes 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                (r,c) = queue.popleft()

                for dr, dc in directions:
                    nR = r + dr
                    nC = c + dc

                    if nR < 0 or nR >= ROWS or nC < 0 or nC >= COLS or grid[nR][nC] == 2 or grid[nR][nC] == 0:
                        continue
                    
                    if grid[nR][nC] == 1:
                        grid[nR][nC] = 2
                        queue.append((nR, nC))
                        fresh -= 1
            minutes += 1
        
    
        return minutes if fresh == 0 else -1



