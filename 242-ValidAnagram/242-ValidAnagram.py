# Last updated: 5/11/2025, 10:41:58 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize an array of 26 elements to track occurrences of letters 'a' - 'z'
        alphabet = [0] * 26

        # iterate through string 's' and increment the letter counts
        # use the ASCII value to map 'a' to index 0, 'b' to index 1, ..., 'z' to index 25
        for char in s:
            index = ord(char) - ord('a')
            alphabet[index] += 1

        # iterate through string 't' and decrement the letter counts
        for char in t:
            index = ord(char) - ord('a')
            alphabet[index] -= 1

        # if all counts are zero, the strings are anagrams
        for count in alphabet:
            if count != 0:
                return False
        return True

        # First loop: increments the count for each character in string 's'
        # Second loop: decrements the count for each character in string 't'
        # If the counts are all zero, the strings are anagrams (same letter counts)