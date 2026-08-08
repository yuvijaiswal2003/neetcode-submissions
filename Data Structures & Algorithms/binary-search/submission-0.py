class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s=0
        e=n-1
        while(s<=e):
            m=e+(s-e)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                s=m+1
            else:
                e=m-1
        return -1