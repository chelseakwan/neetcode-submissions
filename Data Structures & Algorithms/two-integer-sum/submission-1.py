class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # look at first integer, 10 - i = j, if j in list, return index
        for idx, i in enumerate(nums):
            j = target - i
            if j in nums[idx + 1:]:
                return [idx, nums.index(j, idx + 1)]