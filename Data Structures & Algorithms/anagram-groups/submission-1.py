class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            vis=[0]*26
            for c in s:
                vis[ord(c)-ord('a')]+=1
            d[tuple(vis)].append(s)
        return list(d.values())







        