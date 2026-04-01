class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[0]*(2*n)
        for i in range(len(nums)):
            answer[i]=nums[i]
            answer[i+n]=nums[i]
        
        return answer