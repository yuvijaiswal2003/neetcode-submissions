class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        v1=[0]*26
        v2=[]
        for i in range(m+1):
            row=[]
            for j in range(26):
                row.append(0)
            v2.append(row)
        for c in s1:
            v1[ord(c)-ord('a')]+=1
        for i in range(m):
            v2[i+1]=v2[i][:]
            v2[i+1][ord(s2[i])-ord('a')]+=1
        for l in range(m-n+1):
            f=1
            for h in range(26):
                d=v2[l+n][h]-v2[l][h]
                if d!=v1[h]:
                    f=0
                    break
            if f:
                return True
        return False


       
                

                



       
       

        