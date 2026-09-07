class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
       freq={}
       for num in arr1:
        freq[num]=freq.get(num,0)+1
       ans=[]
       for num in arr2:
        if num in freq:
            for _ in range(freq[num]):
                ans.append(num)
            del freq[num]

       for num in sorted(freq):
        for _ in range(freq[num]):
            ans.append(num)
       return ans            