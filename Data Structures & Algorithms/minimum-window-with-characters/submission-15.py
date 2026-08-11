class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""
        hmap = defaultdict(int)
        flag = defaultdict(int)
        for c in t:
            hmap[c] += 1
            flag[c] = 0

        l, r, have, minlen, res = 0, 0, 0, len(s), ""
        while r < len(t):
            if s[r] in flag:
                flag[s[r]] += 1
                have += 1
            r += 1
        if len(t) == have:
            return s[l:r]
        while r < len(s) + 1:
            if len(t) != have:
                if r < len(s) and s[r] in flag:
                    flag[s[r]] += 1
                    have += 1
                r += 1
            else:
                if minlen >= r - l:
                    minlen = r - l
                    res = s[l:r]
                if s[l] in flag:
                    flag[s[l]] -= 1
                    have -= 1
                l += 1

        return res




        