# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # for loop start with last index, stop with -1(-1 is the index before 0, because we want to also access 1st index i.e 0th index we have to stop at -1, because for loop skips last iteration.) and -1 in ending tells that the for should run backwards i.e right to left.

        for i in range(len(digits)-1 , -1, -1):

            # ---------------------------------------------------
            # DRY RUN EXAMPLE 1:
            # digits = [1, 2, 3]
            #
            # i = 2
            # digits[2] = 3
            # Add 1 → 4
            # No carry needed
            # Return [1, 2, 4]
            # ---------------------------------------------------

            # Add 1 to current digit
            digits[i] += 1


            # If digit becomes less than 10:
            # No carry, so answer is ready
            if digits[i] < 10:
                return digits
            
            # ---------------------------------------------------
            # DRY RUN EXAMPLE 2:
            # digits = [1, 2, 9]
            #
            # i = 2
            # 9 + 1 = 10
            #
            # digit becomes 0
            # carry moves left
            #
            # digits = [1, 2, 0]
            # ---------------------------------------------------

            # If digit becomes 10:
            # Set current digit to 0
            # carry automatically goes to next loop (left digit)
            digits[i] = 0


        # ---------------------------------------------------
        # Special case:
        # digits = [9, 9, 9]
        #
        # After loop:
        # [0, 0, 0]
        #
        # Need extra carry:
        # return [1, 0, 0, 0]
        # ---------------------------------------------------

        # If all digits were 9
        # Add 1 at front
        return [1] + digits