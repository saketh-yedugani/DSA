class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        L=0
        R=len(nums)-1
        while L<R:
            nums[L],nums[R]=nums[R],nums[L]
            L+=1
            R-=1
        
        L=0
        R=k-1
        while L<R:
            nums[L],nums[R]=nums[R],nums[L]
            L+=1
            R-=1
        
        L=k
        R=len(nums)-1
        while L<R:
            nums[L],nums[R]=nums[R],nums[L]
            L+=1
            R-=1