class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        i = 0
        j = len(arr) - 1

        ans = []

        while j-i+1 != k:
            if abs(arr[j] - x) > abs(arr[i] - x):
                j -= 1
            elif abs(arr[j] - x) < abs(arr[i] - x):
                i += 1
            else:
                j -= 1       
        
        for i in range(i, j+1):
            ans.append(arr[i])

        return ans