class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = []

        for c,p in zip(capital,profits):
            minCapital.append((c,p))
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c,p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit,-p)
            if not maxProfit:
                break


            w+= -1 * heapq.heappop(maxProfit)
        return w