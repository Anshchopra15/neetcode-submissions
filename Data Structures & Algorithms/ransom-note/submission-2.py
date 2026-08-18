class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = {}

        # Magazine ke characters count karo
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        # RansomNote ke har character ko check karo
        for ch in ransomNote:
            if ch not in freq or freq[ch] == 0:
                return False

            freq[ch] -= 1

        return True 