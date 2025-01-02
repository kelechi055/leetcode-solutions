class Solution(object):
    def containsDuplicate(self, nums):
        checked = set() # make a set to store the checked numbers
      
        for n in nums: # iterate through every number in nums - O(n)
            if n in checked: # check if the current number exists in checked - O(1)
                return True # return true if a duplicate is found
            checked.add(n) # add the current number to the set, since it's not a duplicate - O(1)
        return False # return false if there's no duplicate

        # Time Complexity: O(n)
        # Space Complexity: O(n)
