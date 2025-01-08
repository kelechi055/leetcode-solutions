class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        nums = [] # empty array to store the final result

        for i in range(1, n+1): # iterate through every number from 1 to n - O(n)
            if i % 3 == 0 and i % 5 == 0: # if the number is divisible by 3 and 5, we append "FizzBuzz"
                nums.append("FizzBuzz")
            elif i % 3 == 0: # if the number is divisible by 3, we append "Fizz" - O(1)
                nums.append("Fizz")
            elif i % 5 == 0: # if the number is divisible by 5, we append "Buzz" - O(1)
                nums.append("Buzz") 

            else:
                nums.append(str(i)) # if the number isnt divisible by 3 or 5, we append its string representation
        return nums # return the list of the final result

        # Time Complexity: O(n)
        # Space Complexity: O(n)