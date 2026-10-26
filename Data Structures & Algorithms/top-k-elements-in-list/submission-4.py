class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=1+freq.get(num,0)
        bucket=[[] for _ in range(len(nums)+1)]
        for num , cnt in freq.items():
            bucket[cnt].append(num)
        res=[]

        for count in range(len(nums),0,-1):
            for num in bucket[count]:
                res.append(num)
                if len(res)==k:
                    return res
        
