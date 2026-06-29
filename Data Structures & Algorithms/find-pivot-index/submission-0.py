class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left_sum = right_sum = 0
            for l in range(i):
                left_sum += nums[l]
            for r in range(i+1,len(nums)):
                right_sum += nums[r]
            if left_sum == right_sum:
                return i
        return -1                