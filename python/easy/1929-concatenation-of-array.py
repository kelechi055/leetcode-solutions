class Solution(object):
    def getConcatenation(self, nums):

        ans = []
        for i in range(2): # O(n) - Iterate through twice 
            for n in nums: # O(n) - Iterate for every number in the nums array
                ans.append(n) # O(1) - add every n to our answer array
                
        return ans # Return our answer
        # O(n)