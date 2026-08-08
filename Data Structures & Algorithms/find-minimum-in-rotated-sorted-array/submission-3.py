class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=float('inf')
        s=0
        e=len(nums)-1
        
        while(s<=e):
            m=(s+e)//2
            if nums[s]<=nums[e]:
                ans=min(ans, nums[s])
                break
            if nums[s]<=nums[m]:
                ans=min(ans, nums[s])
                s=m+1
            else:
                ans=min(ans,nums[m])
                e=m-1
        return ans
        