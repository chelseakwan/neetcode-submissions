class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        s_set = set()
        max_len = 0

        while right < len(s):
            if s[right] in s_set:
                s_set.remove(s[left])
                left += 1
            else:
                s_set.add(s[right])
                right += 1
            if len(s_set) > max_len:
                max_len = len(s_set)
        return max_len