class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}

        for num in nums:
            if num in output:
                output[num] += 1
            else:
                output[num] = 1
        
        output = sorted(output.items(), key=lambda item: item[1], reverse = True)
        return [key for key, val in output[:k]]