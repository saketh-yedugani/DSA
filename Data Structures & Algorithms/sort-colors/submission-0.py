class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L,R=0,len(nums)-1
        i=0
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        while i<=R:
            if nums[i]==0:
                swap(L,i)
                L+=1
            elif nums[i]==2:
                swap(R,i)
                R-=1
                i-=1
        
            i+=1    