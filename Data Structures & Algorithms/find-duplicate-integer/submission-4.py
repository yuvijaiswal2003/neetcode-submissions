class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            id=abs(nums[i])-1
            if nums[id]<0:
                return abs(nums[i])
            nums[id]*=-1
        return -1





