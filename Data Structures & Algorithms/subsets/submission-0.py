class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curset = []
        self.helper(0,nums,curset,subsets)
        return subsets

    def helper(self,i,nums,curset,subsets):
        if i>= len(nums):
            subsets.append(curset.copy())
            return
        
        curset.append(nums[i])
        self.helper(i+1,nums,curset,subsets)

        curset.pop()
        self.helper(i+1,nums,curset,subsets)
