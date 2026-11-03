class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d={}
        ans=0
        for num in nums:
            if num in d:
                continue
            left=d.get(num-1,0)
            right=d.get(num+1,0)
            total=left+right+1
            d[num]=total
            d[num-left]=total
            d[num+right]=total
            ans=max(ans,total)
        return ans