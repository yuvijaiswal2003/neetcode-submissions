class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        d = {}
        for ch in t:
            d[ch] = d.get(ch, 0) + 1

        l,r,c=0,0,0

        st = -1
        minl = float('inf')

        while r < n:

            if s[r] in d:
                if d[s[r]] > 0:
                    c += 1
                d[s[r]] -= 1

            while c == m:
                if r - l + 1 < minl:
                    minl = r - l + 1
                    st = l

                if s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] > 0:
                        c -= 1

                l += 1

            r += 1

        if st == -1:
            return ""

        return s[st:st + minl]