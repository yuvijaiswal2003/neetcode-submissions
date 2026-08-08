class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        e=len(nums)-1
        while(s<=e):
            m=(s+e)//2
            if nums[m]==target:
                return m
            
            if target>nums[m]:
                if nums[s]<=nums[m]:
                    s=m+1
                else:
                    if nums[s]>target:
                        s=m+1
                    else:
                        e=m-1
            else:
                if nums[s]>nums[m]:
                        e=m-1
                else:
                    if nums[s]>target:
                        s=m+1
                    else:
                        e=m-1
        return -1