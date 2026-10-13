class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        cache = [[-1]*n for i in range(m)]

        def memoization(r,c):
            if r == m or c == n:
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]
            
            if text1[r] == text2[c]:
                cache[r][c] = 1 + memoization(r+1, c+1)
            else:
                cache[r][c] = max(memoization(r, c+1), memoization(r+1, c))
            return cache[r][c]

        return memoization(0,0)

        