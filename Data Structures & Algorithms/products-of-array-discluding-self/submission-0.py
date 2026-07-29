class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if j!=i:
                    p=p*nums[j]
            ans.append(p)
        return ans


        