class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def memoization(r,c,m,n,cache):
            if r == m or c == n:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m-1 and c == n-1:
                return 1
            
            cache[r][c] = memoization(r+1, c, m, n ,cache) + memoization(r, c+1, m, n ,cache)
            return cache[r][c]
        
        return memoization(0,0,len(obstacleGrid),len(obstacleGrid[0]), [[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))])
        