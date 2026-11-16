class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        high = sum(weights)
        low = max(weights)
        while low<=high :
            currweight = 0
            day = 1
            mid = (low+high)//2
            for i in range(len(weights)):
                if currweight + weights[i] <= mid:
                    currweight += weights[i]
                else:
                    day += 1
                    currweight = weights[i]
            if day<=days:
                high = mid-1
            else:
                low = mid+1
        return low                
