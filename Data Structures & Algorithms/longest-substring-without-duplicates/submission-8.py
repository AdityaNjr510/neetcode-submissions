class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        l, r = 0, 1
        if s:
            hset.add(s[l]) 
        maxlen = 0 if s == "" else 1
        
        while r < len(s):
            if s[r] in hset:
                while s[l] != s[r]:
                    hset.remove(s[l])
                    l += 1
                hset.remove(s[l])
                l += 1
            else:
                hset.add(s[r])
                maxlen = max(r - l + 1, maxlen)
                r += 1
        
        return maxlen