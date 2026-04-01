class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        L=0
        R=len(nums)-1

        while L<=R:
            if nums[L]<nums[R]:
                result = min(result,nums[L])
                break
            mid=(L+R)//2
            result = min(result,nums[mid])
            if nums[mid] >= nums[L]:
                L=mid+1
            else:
                R=mid - 1
        return result