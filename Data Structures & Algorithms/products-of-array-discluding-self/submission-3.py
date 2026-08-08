class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pre=[1]*len(nums)
        suf=[1]*len(nums)
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]
        j=len(nums)-2
        while(j>=0):
            suf[j]=nums[j+1]*suf[j+1]
            j-=1
        for i in range(len(nums)):
            ans[i]=pre[i]*suf[i]
        return ans


        