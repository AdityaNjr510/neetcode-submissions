class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        cmap = {')':'(','}':'{',']':'['}

        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and stack[-1] == cmap[c]:
                stack.pop()
            else:
                return False
        
        return not stack
                
