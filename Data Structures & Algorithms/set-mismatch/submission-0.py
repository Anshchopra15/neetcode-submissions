class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        duplicate = 0
        missing = 0
        
        for num in range(1,n+1):
            if freq.get(num,0)==2:
                duplicate = num
            elif freq.get(num,0)==0:
                missing = num

        return [duplicate,missing]                