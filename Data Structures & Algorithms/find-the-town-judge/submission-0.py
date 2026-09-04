class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusttox = [0]*(n+1)
        trustbyx = [0]*(n+1)
        for a,b in trust:
            trusttox[b] += 1
            trustbyx[a] += 1

        for person in range(1,n+1):
            if trustbyx[person]==0 and trusttox[person]==n-1:
                return person
        return -1        
