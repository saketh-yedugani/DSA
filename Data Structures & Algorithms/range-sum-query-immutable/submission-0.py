class NumArray:

    def __init__(self, nums: List[int]):
        self.presum=[]
        total=0
        for i in nums:
            total += i
            self.presum.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        right_val=self.presum[right]
        if left>0:
            left_val=self.presum[left-1]
        else:
            left_val=0
        return (right_val-left_val)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)