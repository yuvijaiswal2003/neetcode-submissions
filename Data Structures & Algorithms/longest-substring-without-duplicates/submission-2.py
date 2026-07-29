class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        l,r=0,0
        vis=[0]*128
        while(r<len(s)):
           
            
            if vis[ord(s[r])-ord('a')]==0:
                vis[ord(s[r])-ord('a')]+=1
                maxlen=max(maxlen,r-l+1)
                r+=1
            else:
                r=l+1
                l+=1
                vis=[0]*128

        return maxlen







        