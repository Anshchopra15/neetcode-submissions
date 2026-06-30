class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0 
        new_arr = set(nums)
        for num in nums:
            curr = num
            streak = 0
            while curr in new_arr:
                curr = curr+1
                streak = streak+1
            count = max(count,streak)
        return count        