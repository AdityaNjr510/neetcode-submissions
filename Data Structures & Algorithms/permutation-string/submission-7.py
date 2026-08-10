class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        main_flag = defaultdict(int)
        flag = defaultdict(int)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for c in alpha:
            main_flag[c], flag[c] = 0, 0
        for c in s1:
            main_flag[c] += 1
        l = 0

        for r in range(len(s1)):
            flag[s2[r]] += 1
        while r + 1 <= len(s2):
            print(flag)
            if main_flag == flag:
                return True
            l, r = l + 1, r + 1
            if r < len(s2):
                flag[s2[r]] += 1
                flag[s2[l - 1]] -= 1
        
        return False
            

        