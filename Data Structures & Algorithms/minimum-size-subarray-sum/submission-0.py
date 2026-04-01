class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L=0
        sum=0
        #sum += nums[L]
        result= float('inf')
        for R in range(len(nums)):
            sum += nums[R]
            while sum >=target:
                result = min(result,R-L+1)
                sum -= nums[L]
                L+=1
        if result==float('inf'):
            return 0
        else:
            return result
            

