class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visit = set()
        queue = deque()

        queue.append((0,0))
        visit.add((0,0))

        directions = [(0,1),(0,-1), (1,1),(-1,-1),(1,0),(-1,0),(1,-1),(-1,1)]
        pathLength = 1

        while queue:
            for i in range(len(queue)):
                (r,c) = queue.popleft()
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return pathLength
                for dr, dc in directions:
                    newRow = r+dr
                    newCol = c + dc
                    if newRow < 0 or newCol < 0 or newRow >= len(grid) or newCol >= len(grid[0]) or grid[newRow][newCol] == 1 or (newRow, newCol) in visit:
                        continue
                    queue.append((newRow, newCol))
                    visit.add((newRow, newCol))
            pathLength += 1
        
        return -1 

        