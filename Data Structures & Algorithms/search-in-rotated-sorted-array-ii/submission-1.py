class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L=0
        R=len(nums) - 1

        while L<=R:
            mid =L+(R-L) // 2
            if target == nums[mid]:
                return True
            
            if nums[L] < nums[mid]:
                if target < nums[mid] and target >= nums[L]:
                    R = mid - 1
                else:
                    L = mid + 1
            elif nums[L] > nums[mid]:
                if target > nums[mid] and target <= nums[R]:
                    L = mid+1
                else:
                    R=mid-1
            else:
                L+=1
        return False
