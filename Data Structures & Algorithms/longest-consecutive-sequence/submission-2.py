class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hasset=set(nums)
        maxlen=0
        length=0
        for num in nums:
            if num-1 not in  hasset:
                length=1
                while num+length in hasset:
                    length+=1
                maxlen=max(maxlen,length)
        return maxlen



        
            
