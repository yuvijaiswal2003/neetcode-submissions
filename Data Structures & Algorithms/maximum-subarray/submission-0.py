class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxsum=float('-inf')
        for num in nums:
            sum+=num
            if sum>maxsum:
                maxsum=sum
            if sum<0:
                sum=0
        return maxsum