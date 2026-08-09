class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1

        def check_val(char):
            return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')


        while left < right:
            while left < right and check_val(s[left]) == False:
                left += 1
            while left < right and check_val(s[right]) == False:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
