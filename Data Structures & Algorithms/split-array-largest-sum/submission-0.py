class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            cursum = 0
            for n in nums:
                cursum += n
                if cursum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    cursum = n
            return True #subarray + 1 <= k
        
        L = max(nums)
        R = sum(nums)
        result = R
        while L <= R:
            mid = L + ((R - L) // 2)
            if canSplit(mid):
                result = mid
                R = mid - 1
            else:
                L = mid + 1
        return result