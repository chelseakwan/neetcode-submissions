class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [0] * len(arr)

        for i in range(len(arr) - 1):
            output[i] = max(arr[i + 1:])
        output[-1] = -1
        return output