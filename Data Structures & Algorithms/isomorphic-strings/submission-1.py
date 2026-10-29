class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # first check str length, if diff length > false
        if len(s) != len(t):
            return False
        
        # create a dictionary map, s > t
        mapST, mapTS = {}, {}
        for i in range(len(s)):
            s_char, t_char = s[i], t[i]
            if ((s_char in mapST and mapST[s_char] != t_char) or (t_char in mapTS and mapTS [t_char] != s_char)):
                return False
            mapST[s_char] = t_char
            mapTS[t_char] = s_char

        return True