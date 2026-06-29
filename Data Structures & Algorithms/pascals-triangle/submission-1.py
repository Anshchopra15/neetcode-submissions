class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            curr = [1]
            for j in range(0,i-1):
                curr.append(ans[-1][j]+ans[-1][j+1])
            if i>0: 
                curr.append(1)

            ans.append(curr)
        return ans                 