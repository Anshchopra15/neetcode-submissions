class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = []
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i]<heights[j]:
                    min_index = i
                else:
                    min_index = j    
                volume.append((j-i)*heights[min_index])
        return max(volume)        