class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        for words in strs:
          keys = "".join(sorted(words))

          if keys not in d:
              d[keys] = []

          d[keys].append(words)

        return list(d.values())