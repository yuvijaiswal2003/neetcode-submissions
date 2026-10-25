class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        d2={}
        for k in s:
            d1[k]=1+d1.get(k,0)
        for j in t:
            d2[j]=1+d2.get(j,0)

        for i in s:
            if i not in d2 or d1[i]!=d2[i]:
                return False
        return True