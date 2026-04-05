class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        for i in range(len(arr)):
            res = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > res:
                    res = arr[j]
            arr[i] = res
        arr[-1] = -1
        return arr