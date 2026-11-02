class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a window of len(s1)
        left = 0
        right = len(s1)

        # check the window to see if it matches
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s2) - len(s1) + 1):
            count = Counter(s1)
            
            if count == Counter(s2[left:right]):
                return True
            else:
                left += 1
                right += 1
        return False