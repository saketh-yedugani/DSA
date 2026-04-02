class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curset= []
        subset= []
        nums.sort()
        self.dfs(0,nums,curset,subset)
        return subset

    def dfs(self,i,nums,curset,subset):
        if i>=len(nums):
            subset.append(curset.copy())
            return
        
        curset.append(nums[i])
        self.dfs(i+1,nums,curset,subset)

        curset.pop()
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        self.dfs(i+1,nums,curset,subset)