class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        arr = arr.copy()
        while k>0:
            closest = arr[0]
            for i in range(1,len(arr)):
                if abs(arr[i]-x) < abs(closest-x):
                    closest = arr[i]
                elif abs(arr[i]-x) == abs(closest-x) and arr[i]<closest :
                    closest = arr[i]
            result.append(closest)
            arr.remove(closest)
            k-=1
        result.sort()
        return result                            