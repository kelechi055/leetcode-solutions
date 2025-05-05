# Last updated: 5/4/2025, 8:34:51 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = set()


        # nums [1, 0, 1]
        # checked [1, 0, ]
        for i in nums:
            if i in checked:
                return True
            checked.add(i)
        return False
        # return false

        # false
        # false
        # True




