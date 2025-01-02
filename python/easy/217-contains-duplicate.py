class Solution(object):
    def containsDuplicate(self, nums):
        checked = set()

        # iterate through every number in nums
        for n in nums: # O(n)
            #if that number is already in checked, return false, then add it to the checked hashset()
            if n in checked: # O(n) or O(1)
                return True # O(1)
            checked.add(n) # O(1)
        return False # O(1)

        #Time Complexity: O(n)
