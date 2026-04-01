class Solution:
    def mySqrt(self, x: int) -> int:
        L = 0
        R = x
        result = 0

        while L<=R:
            mid = L+((R-L) // 2)
            if mid ** 2 > x:
                R = mid - 1
            elif mid ** 2 < x:
                L = mid + 1
                result = mid
            else:
                return mid
        return result