class Solution(object):
    def runningSum(self, nums): 
        for n in range(1, len(nums)): #iterate through eveyr number from 1 to the length of nums
            nums[n] += nums[n -1]
        return nums

    #Time Complexity: O(n)