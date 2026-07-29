class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxlen=0
        for i in range(len(s)):
            count={}
            maxf=0
            for j in range(i, len(s)):
                count[s[j]]=1+count.get(s[j],0)
                maxf=max(maxf,count[s[j]])
                if (j-i+1)-maxf<=k:
                    maxlen=max(maxlen,j-i+1)
                else:
                    break
        return maxlen

