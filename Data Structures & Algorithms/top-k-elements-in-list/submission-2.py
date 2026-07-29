class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        bucket=[[] for _ in range(len(nums)+1)]
        for num, count in d.items():
            bucket[count].append(num)
        ans=[]
        for i in range(len(nums),0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
