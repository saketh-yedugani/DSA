class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num=[]
        for i in nums:
            num.append(-1*i)
        heapq.heapify(num)
        res = []
        while k>0:
            res.append(heapq.heappop(num))
            k-=1
        return -1*res[-1]