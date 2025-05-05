# Last updated: 5/4/2025, 8:42:34 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif sorted(s) != sorted(t):
            return False
        return True