class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsfreq = {}
        for ch in chars:
            charsfreq[ch] = charsfreq.get(ch,0)+1
        ans = 0
        for word in words:
            wordfreq = {}
            for ch in word:
                wordfreq[ch] = wordfreq.get(ch,0)+1
            good = True
            for ch in wordfreq:
                if wordfreq[ch] > charsfreq.get(ch,0):
                    good = False
                    break
            if good:
                ans += len(word)
        return ans                        