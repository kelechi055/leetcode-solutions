# Last updated: 5/12/2025, 5:54:54 PM
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        checked = set()
        count = 0

        # generate all 3-digit permutations (one by one) using given digits
        for val in itertools.permutations(digits, 3):
            # build the number by placing each digit in the correct place (hundreds, tens, ones)
            number = val[0] * 100 + val[1] * 10 + val[2]
            # build the number from the digits
            if val[0] != 0 and val[2] % 2 == 0:
                # count each number only once
                if number not in checked:
                    count+=1
                checked.add(number)
        return count

        # Time Complexity: O(n!)

        # Notes:
        # permutations([1, 2, 3], 3) generates all the 3-digit permutations of the digits:
        # (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)
        # Here, [1, 2, 3] are the digits, and 3 is the number of digits to permute.
