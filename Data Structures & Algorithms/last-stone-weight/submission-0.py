class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stn=[]
        for s in stones:
            stn.append(-1*s)
        heapq.heapify(stn)

        while len(stn) > 1:
            first = heapq.heappop(stn)
            second = heapq.heappop(stn)
            if second > first:
                heapq.heappush(stn,first-second)
        
        stn.append(0)
        return abs(stn[0])
