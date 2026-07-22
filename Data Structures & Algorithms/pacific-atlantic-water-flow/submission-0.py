class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        Rows , Cols = len(heights), len(heights[0])

        def dfs(r,c,visit,prevheight):
            if(r<0 or c<0 or r>=Rows or c>= Cols or (r,c) in visit or heights[r][c]<prevheight):
                return
            visit.add((r,c))    
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(Cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(Rows-1,c,atlantic,heights[Rows-1][c])

        for r in range(Rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,Cols-1,atlantic,heights[r][Cols-1])

        res = []
        for r in range(Rows):
            for c in range(Cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res               