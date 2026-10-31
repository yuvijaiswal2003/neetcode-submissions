class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for num in nums:
            d[num]=1+d.get(num,0)
        bucket=[[] for _ in range(len(nums)+1)]
        for key,value in d.items():
            bucket[value].append(key)

        for cnt in range(len(nums),0,-1):
            for num in bucket[cnt]:
                ans.append(num)
                if len(ans)==k:
                    return ans
        



        