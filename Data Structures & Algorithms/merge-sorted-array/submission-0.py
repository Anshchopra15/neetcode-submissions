class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t=0
        for i in range(len(nums1)):
            if nums1[i] == 0:
                for j in range(t,len(nums2)):
                    nums1[i] = nums2[j]
                    t+=1
                    break
        nums1.sort()           