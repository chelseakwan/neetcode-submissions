class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        res = []
        dict = sorted(dict.items(), key=lambda item:item[1], reverse = True)
        for i in range(k):
            res.append(dict[i][0])

        return res