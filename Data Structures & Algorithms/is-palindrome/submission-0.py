class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        
        for i in range(round(len(s) / 2)):
            while i <= len(s) / 2:
                if s[0 + i].lower() != s[len(s) - 1 - i].lower():
                    return False
                i += 1
        return True