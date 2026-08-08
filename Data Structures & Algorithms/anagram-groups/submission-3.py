class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = collections.defaultdict(list)
        # list : string

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(s)

        return list(hashmap.values())