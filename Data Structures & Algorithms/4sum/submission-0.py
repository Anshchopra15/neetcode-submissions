class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for p in range(k+1,n):
                        if (nums[i] + nums[j] + nums[k] + nums[p] == target):
                            quad = [nums[i],nums[j],nums[k],nums[p]]

                            if quad not in arr:
                                arr.append(quad)

        return arr                        