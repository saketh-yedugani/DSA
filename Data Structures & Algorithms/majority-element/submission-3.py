class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        checker=defaultdict(int)
        res= maxCount=0
        for i in range(len(nums)):
            #if nums[i] in checker:
            checker[nums[i]] += 1
            if maxCount < checker[nums[i]]:
                res=nums[i]
                maxCount=checker[nums[i]]
            #else:
            #    checker[nums[i]] = 1
        print(checker)
        return res