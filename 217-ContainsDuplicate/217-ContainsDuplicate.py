# Last updated: 5/4/2025, 8:29:23 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()


        # [1, 2, 1]
        # [1]
        for i in nums:
            if i in checked:
                return True
            checked.add(i)
        return False

        #false
        #false
        #true


