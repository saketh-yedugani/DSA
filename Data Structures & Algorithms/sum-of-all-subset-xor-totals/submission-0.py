class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i,total):
            if i == len(nums):
                return total
            return dfs(i+1,total ^ nums[i]) + dfs(i+1,total)        
            # total^nums[i] includes the number in the total
            #just total indicates we didnt include in the total
        return dfs(0,0)
