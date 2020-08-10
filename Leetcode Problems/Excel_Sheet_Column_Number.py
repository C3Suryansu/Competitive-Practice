class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        res = 0
        for i in range(len(s)):
            res += (ord(s[i]) - 64) * 26**i
        return res
