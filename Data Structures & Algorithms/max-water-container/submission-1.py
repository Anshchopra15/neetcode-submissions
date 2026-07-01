class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i]<heights[j]:
                    min_index = i
                else:
                    min_index = j    
                area.append((j-i)*heights[min_index])
        return max(area)        