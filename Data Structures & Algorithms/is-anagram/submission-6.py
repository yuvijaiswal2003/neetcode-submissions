class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        vis=[0]*26

        for k in s:
            vis[ord(k)-ord('a')]+=1
        for j in t:
            vis[ord(j)-ord('a')]-=1
        for i in range(26):
            if vis[i]!=0:
                return False

        return True
