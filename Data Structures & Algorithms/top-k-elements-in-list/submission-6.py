class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for num in nums:
            d[num]=1+d.get(num,0)
        sorted_dict=dict(sorted(d.items(), key=lambda x:x[1]))
        stack=[]
        for key in sorted_dict.keys():
            stack.append(key)
        while k:
            ans.append(stack.pop())
            k-=1
        return ans


        