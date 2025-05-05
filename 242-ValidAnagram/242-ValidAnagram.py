# Last updated: 5/4/2025, 8:41:29 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) != sorted(t):
            return False
        return True