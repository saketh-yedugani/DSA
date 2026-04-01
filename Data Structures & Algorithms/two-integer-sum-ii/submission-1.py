class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            checker=target-numbers[i]
            for j in range(i+1,len(numbers)):
                if numbers[j] == checker:
                    return [i+1,j+1]
        return []