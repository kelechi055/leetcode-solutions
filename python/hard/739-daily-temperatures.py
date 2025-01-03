class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []  # create an empty stack to keep track of the indices of the temperatures
        counter = 0  # initialize a counter to count the days until a warmer temperature
        
        # loop through the temperatures
        for n in temperatures:
            # nested loop to compare each temperature with the others
            for j in temperatures:
                # if the next day's temperature is warmer, increment the counter
                if temperatures[n+1] > temperatures[j]:
                    counter += 1
                j += 1  # increment the inner loop counter
            n += 1  # increment the outer loop counter
        
        # time complexity is O(n^2) due to the nested loops