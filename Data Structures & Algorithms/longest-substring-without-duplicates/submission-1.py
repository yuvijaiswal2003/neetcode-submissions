class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        for i in range(len(s)):
            vis=[0]*128
            for j in range(i , len(s)):
                if vis[ord(s[j])-ord('a')]==0:
                    vis[ord(s[j])-ord('a')]+=1
                    maxlen=max(maxlen,j-i+1)
                else:
                    break
           
        return maxlen





        