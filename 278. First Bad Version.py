# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:

# Input: n = 1, bad = 1
# Output: 1
 

# Constraints:

# 1 <= bad <= n <= 231 - 1

# The isBadVersion API is already given by LeetCode
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # Search range starts from version 1 to version n
        left = 1
        right = n

        # Keep searching while valid range exists
        while left <= right:

            # Find middle version
            mid = (left + right) // 2

            # ---------------------------------------------------
            # DRY RUN:
            # n = 5
            # bad version = 4
            #
            # Versions: 1 2 3 4 5
            #
            # left = 1, right = 5
            # mid = 3
            # isBadVersion(3) = False
            # → first bad must be on right side
            # left = 4
            #
            # left = 4, right = 5
            # mid = 4
            # isBadVersion(4) = True
            # → could be answer, but maybe earlier bad exists
            # right = 3
            #
            # Loop ends:
            # left = 4, right = 3
            # return left = 4
            # ---------------------------------------------------

            # If current version is bad
            if isBadVersion(mid):

                # mid might be first bad,
                # but there could be earlier bad versions
                # so search LEFT side
                right = mid - 1

            else:
                # Current version is good,
                # so first bad must be after mid
                left = mid + 1

        # When loop ends:
        # left points to first bad version
        return left
    
# note: this problem is similar to problem no. 35 Search_Insert_position