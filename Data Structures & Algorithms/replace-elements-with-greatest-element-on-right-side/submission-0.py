class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            maxarr = []
            for j in range(i+1,len(arr)):
                maxarr.append(arr[j])
            maxele = max(maxarr)
            arr[i] = maxele
        arr[-1] = -1
        return arr