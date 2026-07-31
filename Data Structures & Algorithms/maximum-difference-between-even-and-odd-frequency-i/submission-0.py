class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        maxodd = float("-inf")
        mineven = float("inf")   

        for count in freq.values():
            if count % 2 == 1:
                maxodd = max(maxodd,count)
            else:
                mineven = min(mineven,count)
        return maxodd - mineven             