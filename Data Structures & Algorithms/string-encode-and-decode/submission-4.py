class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            j=i

            while s[j]!="#":
                j=j+1
            k=int(s[i:j])
            new=s[j+1:j+1+k]
            ans.append(new)
            i=j+1+k
        return ans

