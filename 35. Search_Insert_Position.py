# Problem Statement
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Two pointer approach
        left = 0
        right = len(num) - 1
        # left = 0   → first index
        # right = 3  → last index

        while left <= right:
            mid = (left + right) // 2
            # Why?
            # We want to check middle element.



            if nums[mid] == target:
                return mid
            #Case 1: target found
            # nums = [1, 3, 5, 6]
            # target = 5
            # mid = 2
            # nums[2] = 5
            # Found → return 2
            
            elif nums[mid] < target:
                left = mid + 1
            # Because:
            # Everything left of mid is smaller too
            # So target must be on the right side.

            else:
                right = mid - 1

            # Case 3: Target is smaller
            # So target must be on left side.

        return left
        # If target not found:
        # 'left' is the correct insert position





        # ---------------------------------------------------
            # FULL DRY RUN EXAMPLE:
            #
            # nums = [1, 3, 5, 6]
            # target = 2
            #
            # Initial:
            # left = 0, right = 3
            #
            # Iteration 1:
            # mid = (0 + 3) // 2 = 1
            # nums[mid] = nums[1] = 3
            #
            # Compare:
            # target = 2 < 3
            # so target must be on left side
            #
            # Update:
            # right = mid - 1 = 0
            #
            # Now:
            # left = 0, right = 0
            #
            # -----------------------------------
            # Iteration 2:
            #
            # mid = (0 + 0) // 2 = 0
            # nums[mid] = nums[0] = 1
            #
            # Compare:
            # target = 2 > 1
            # so target must be on right side
            #
            # Update:
            # left = mid + 1 = 1
            #
            # Now:
            # left = 1, right = 0
            #
            # Loop ends because:
            # left > right
            #
            # Final:
            # left = 1
            #
            # Meaning:
            # target should be inserted at index 1
            #
            # nums becomes conceptually:
            # [1, (2), 3, 5, 6]
            #      ↑
            #      index 1
            # ---------------------------------------------------




# note: 
# The loop condition:

# while left <= right:

# does only one thing:

# 👉 decides whether to run the loop again

# It does NOT change left or right.

# 🔍 Step-by-step for your example
# nums = [1, 3, 5, 6]
# target = 2
# Initial
# left = 0
# right = 3

# Condition:

# 0 <= 3 → True

# Loop runs.

# Iteration 1
# mid = (0 + 3) // 2 = 1
# nums[mid] = 3

# Since:

# 2 < 3

# Run:

# right = mid - 1

# Now:

# left = 0
# right = 0
# Check loop again
# 0 <= 0 → True

# Loop runs again.

# Iteration 2
# mid = (0 + 0) // 2 = 0
# nums[mid] = 1

# Since:

# 2 > 1

# Run:

# left = mid + 1

# Now:

# left = 1
# right = 0

# 👉 This is when left becomes 1.

# Check loop again

# Condition:

# 1 <= 0 → False

# Loop stops.