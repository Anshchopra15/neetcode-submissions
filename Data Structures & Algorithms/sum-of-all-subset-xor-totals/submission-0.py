class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        ans = []
        def recursion(start):
            ans.append(subset.copy())
            for i in range(start,len(nums)):
                subset.append(nums[i])
                recursion(i+1)
                subset.pop()
        recursion(0) 
        total = 0
        for sub in ans:
            xor = 0
            for num in sub:
                xor = xor^num
            total = total+xor
        return total                   