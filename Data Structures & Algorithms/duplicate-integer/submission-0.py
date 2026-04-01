class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countdict=defaultdict(int)
        for i in nums:
            if i not in countdict:
                countdict[i] = 1
            else:
                return True

        return False    