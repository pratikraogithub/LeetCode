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