class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i, j = 0, 1
        while i < len(s):
            while j < len(s) and s[j] != '#':
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + length + 1
            j = i + 1

        return res
