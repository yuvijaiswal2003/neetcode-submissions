class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1={}
        n=len(s1)
        m=len(s2)
        f=1
        maxf=1
        for i in range(n):
            if s1[i] not in d1:
                d1[s1[i]]=1
            else:
                d1[s1[i]]+=1
        for j in range(m-n+1):
            d2={}
            f=1
            res=""
            for k in range(j,j+n):
                res+=s2[k]
            for l in res:
                if l not in d2:
                    d2[l]=1
                else:
                    d2[l]+=1
            for p in s1:
                if p not in d2 or d1[p]!=d2[p]:
                    f=0
                else:
                    f+=1
                    maxf=max(f,maxf)
        if maxf!=n+1:
            return False
        return True

        