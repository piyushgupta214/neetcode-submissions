class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        originalColor = image[sr][sc]
        
        def dfs(r: int, c: int):
            ROW = len(image)
            COL = len(image[0])
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            if image[r][c] != originalColor or image[r][c] == color:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            
        
        dfs(sr, sc)
        return image

        