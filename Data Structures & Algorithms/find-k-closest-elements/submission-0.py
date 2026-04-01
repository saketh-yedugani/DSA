class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = len(arr) - k
        while L<R:
            m = (L+R) // 2
            if x-arr[m] > arr[m+k] - x:
                L = m+1
            else:
                R = m
        return arr[L:L+k]