class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        l,r=0,0
        vis=[0]*128
        while r<len(s):
            if vis[ord(s[r])]==0:
                vis[ord(s[r])]=1
                maxlen=max(maxlen, r-l+1)
                r=r+1
            else:
                vis[ord(s[l])]=0
                l=l+1
        return maxlen
