class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalmax, globalmin = nums[0], nums[0]
        curMax, curMin = 0,0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globalmax = max(globalmax,curMax)
            globalmin = min(globalmin, curMin)
        
        if globalmax > 0:
            return max(globalmax, total-globalmin)
        else:
            return globalmax