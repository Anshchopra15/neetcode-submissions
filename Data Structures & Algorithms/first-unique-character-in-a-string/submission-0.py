class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            unichar = True

            for j in range(len(s)):
                if i != j and s[i] == s[j]:
                    unichar = False
                    break

            if unichar:
                return i

        return -1              