class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch.lower()
        for i in range(len(new)):
             j = len(new)-1-i
             if new[i]!=new[j]:
                  return False 
        return True                