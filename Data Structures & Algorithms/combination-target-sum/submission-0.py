class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans =[]
        def dfs(index,path,target):
            if target == 0:
                ans.append(path.copy())
                return
            if target < 0 or index == len(nums):
                return
            path.append(nums[index])
            dfs(index , path , target-nums[index])   
            path.pop()
            dfs(index+1 , path , target)
        dfs(0,[],target)
        return ans             