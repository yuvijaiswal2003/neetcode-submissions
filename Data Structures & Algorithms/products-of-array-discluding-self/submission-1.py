class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        p=1
        zero=0
        for num in nums:
            if num==0:
                zero+=1
            else:
                p=p*num
        for num in nums:
            if zero>1:
                ans.append(0)
            elif zero==1:
                if num==0:
                    ans.append(p)
                else:
                    ans.append(0)
            else:
                ans.append(p//num)
        return ans


        