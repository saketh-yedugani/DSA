class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i,curcomb,total):
            if total == target:
                result.append(curcomb.copy())
                return
            if i>=len(nums) or total>target:
                return
            
            curcomb.append(nums[i])
            dfs(i,curcomb,total+nums[i])

            curcomb.pop()
            dfs(i+1,curcomb,total)
        
        dfs(0,[],0)
        return result