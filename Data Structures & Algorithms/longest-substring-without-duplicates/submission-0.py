class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_st = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            st = len(seen)
            max_st = max(max_st,st)
        return max_st        