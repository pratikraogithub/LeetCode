# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # Search space is from 1 to n
        left = 1
        right = n

        # Keep searching while valid range exists
        while left <= right:

            # Find middle number
            mid = (left + right) // 2

            # Ask API about current guess
            result = guess(mid)

            # ---------------------------------------------------
            # DRY RUN:
            # n = 10
            # hidden number = 6
            #
            # left = 1, right = 10
            # mid = 5
            # guess(5) = 1  (too low)
            # → search right
            #
            # left = 6, right = 10
            # mid = 8
            # guess(8) = -1 (too high)
            # → search left
            #
            # left = 6, right = 7
            # mid = 6
            # guess(6) = 0
            # → found answer
            # ---------------------------------------------------

            # Case 1: guessed correctly
            if result == 0:
                return mid

            # Case 2: guess too low
            elif result == 1:
                left = mid + 1

            # Case 3: guess too high
            else:
                right = mid - 1