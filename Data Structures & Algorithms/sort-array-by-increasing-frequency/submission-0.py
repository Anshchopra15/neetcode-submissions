class Solution:
    def frequencySort(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        def sort_key(x):
            return (freq[x], -x)

        nums.sort(key=sort_key)

        return nums  