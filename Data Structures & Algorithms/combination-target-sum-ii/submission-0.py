class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()

        result = []
        path = []

        def dfs(index, target):

            if target == 0:
                result.append(path.copy())
                return

            if index >= len(candidates) or target < 0:
                return

            path.append(candidates[index])
            dfs(index + 1, target - candidates[index])
            path.pop()

            next_index = index + 1

            while (next_index < len(candidates) and
                   candidates[next_index] == candidates[index]):
                next_index += 1

            dfs(next_index, target)

        dfs(0, target)
        return result     