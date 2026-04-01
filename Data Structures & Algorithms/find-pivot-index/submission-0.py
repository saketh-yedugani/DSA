class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumnum=[]
        res=0
        for i in nums:
            res += i
            sumnum.append(res)
        
        l=0
        r=len(nums)-1
        #right_val=sumnum[r]
        while l<=r:
            if l>0:
                left_val=sumnum[l-1]
                right_val=sumnum[r]-sumnum[l]
            else:
                left_val=0
                right_val=sumnum[r]-sumnum[l]
            
            if left_val==right_val:
                return l
            l +=1
        return -1
