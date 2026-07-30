class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [[grid[0][0],0,0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        visit.add((0,0))
        while minHeap:
            t,r,c = heapq.heappop(minHeap)

            if r == N-1 and c == N-1:
                return t
            for dr, dc in directions:
                neidr, neidc = r+dr,c+dc
                if (neidr<0 or neidc<0 or neidr==N
                or neidc==N or (neidr,neidc) in visit):
                    continue
                visit.add((neidr,neidc))
                heapq.heappush(minHeap,[max(t,grid[neidr][neidc]),neidr,neidc])
