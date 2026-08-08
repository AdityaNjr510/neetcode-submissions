class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap1 = collections.defaultdict(int)
        hashmap2 = collections.defaultdict(int)

        for i in s:
            hashmap1[i] += 1

        for i in t:
            hashmap2[i] += 1
        
        return hashmap1 == hashmap2
