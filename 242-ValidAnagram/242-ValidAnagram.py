# Last updated: 5/11/2025, 10:41:10 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize an array of 26 elemets to track occurences of letters 'a' - 'z'
        alphabet = [0] * 26

        # iterate through stirng 's' and increment the letter counts
        # use the ASCII value to map 'a' to index 0, 'b' to index 1, ..., 'z' to index 25

        for char in s:
            # make the index the ordinal of each character 'a'
            index = ord(char) - ord('a')
            alphabet[index]+=1

        # iterate through stirng 't' and decrement the letter counts
        for char in t:
            # make the index the ordinal of each character 'a'
            index = ord(char) - ord('a')
            alphabet[index]-=1

        # if all counts are zero, the strings are anagrams
        for i in alphabet:
            if i != 0:
                return False
        return True

        # Time Complexity: O(n)

        # first loop:
        # subtracts 1 to the index of each letter in string "s"

        # second loop:
        # subtracts 1 to the index of each letter in string "t"

        # to find out if its an anagram:
        # if each index = 0, that means stirng "s" and string "t" have thesame letter counts.