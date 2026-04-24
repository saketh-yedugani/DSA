class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid),len(grid[0])
        q=collections.deque()
        visit=set()

        def addVal(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]==-1 or (r,c) in visit):
                return
            q.append([r,c])
            visit.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=distance
                addVal(r+1,c)
                addVal(r-1,c)
                addVal(r,c+1)
                addVal(r,c-1)
            distance += 1
