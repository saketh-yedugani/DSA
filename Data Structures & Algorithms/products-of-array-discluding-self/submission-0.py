class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=deque([])
        output=[]

        prefix_pro=1
        postfix_pro=1
        for i in range(len(nums)):
            prefix_pro*=nums[i]
            prefix.append(prefix_pro)
        for j in range(len(nums)-1,-1,-1):
            #print(postfix_pro,"before")
            postfix_pro*=nums[j]
            #print(postfix_pro,"after")
            postfix.appendleft(postfix_pro)
        for k in range(len(nums)):
            if k==0:
                output.append(postfix[k+1])
            elif k==len(nums)-1:
                output.append(prefix[k-1])
            else:
                output.append(prefix[k-1]*postfix[k+1])
        print(prefix,"prefix")
        print(postfix,"postfix")
        return output
