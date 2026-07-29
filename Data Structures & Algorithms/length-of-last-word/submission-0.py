class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        count = 0
        for ch in s:
            count += 1
            if ch == ' ':
                count = 0
        return count
