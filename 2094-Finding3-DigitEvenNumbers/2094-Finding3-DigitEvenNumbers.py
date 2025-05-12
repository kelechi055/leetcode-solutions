# Last updated: 5/12/2025, 6:27:40 PM
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
        checked = set()

        numbers = []

        for val in itertools.permutations(digits, 3):

            # make sure the number doesnt start with 0 and is even
            if val[0] == 0:
                continue
            if val[2] % 2 == 0:
                number = val[0] * 100 + val[1] * 10 + val[2] 
                if number not in checked:
                    numbers.append(number)
                    checked.add(number)

        return sorted(numbers)

