class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            index = -1
            for i in range(len(nums2)):
                if nums2[i] == num:
                    index = i
                    break

            nextgreater = -1
            for j in range(index+1,len(nums2)):
                if nums2[j] > num:
                    nextgreater = nums2[j]   
                    break

            ans.append(nextgreater)   
        return ans          