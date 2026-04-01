class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        checker=defaultdict(int)
        for i in nums:
            checker[i] += 1
        
            if len(checker)<=2:
                continue
            new_checker=defaultdict(int)
            for num, c in checker.items():
                if c > 1:
                    new_checker[num] = c-1
            checker=new_checker
        
        result=[]
        for n in checker:
            if nums.count(n) > len(nums) // 3:
                result.append(n)
        
        return result