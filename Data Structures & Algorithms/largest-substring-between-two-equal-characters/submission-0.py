class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        first = {}
        ans = -1

        for i in range(len(s)):

            if s[i] in first:
                length = i - first[s[i]] - 1
                ans = max(ans, length)

            else:
                first[s[i]] = i

        return ans    