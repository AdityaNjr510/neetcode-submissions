class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        if s == "":
            return 0
        l, r = 0, 1
        hmap = defaultdict(int)
        hmap[s[l]] += 1
        maxv = 1
        res = 1

        while r < len(s):
            hmap[s[r]] += 1
            maxv = max(hmap[s[r]], maxv)
            if (r - l + 1) - maxv > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
            r += 1

        return res





