class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        vis=[0]*26
        for i in range(len(s)):
            vis[ord(s[i])-ord('a')]+=1
        for j in range(len(t)):
            vis[ord(t[j])-ord('a')]-=1
        for k in range(26):
            if vis[k]!=0:
                return False
        return True


            
