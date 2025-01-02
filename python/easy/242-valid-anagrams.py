class Solution(object):
    def isAnagram(self, s, t):
        
        # if the length of s and t are not the same, they cant be anagrams O(1) 
        if len(s) != len(t): # O(1)
            return False 
        # sort both strings and compare
        # If they are not the same, s and t are not anagrams
        if sorted(s) != sorted(t): # O(n log n) 
            return False
        #If none of the conditions above are met, s and t are anagrams. O(1)
        return True 

        #Time Complexity is O(n log n)