class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        ans = []
        def recursion(start):
            ans.append(subset.copy())
            for i in range(start , len(nums)):
                subset.append(nums[i])
                recursion(i+1)
                subset.pop()
        recursion(0)
        return ans