class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Step 1: Sort the array
        # Sorting helps in:
        # 1. Using two-pointer technique
        # 2. Easily skipping duplicates
        nums.sort()

        # This will store the final list of unique triplets
        result = []

        # Step 2: Iterate through the array
        for i in range(len(nums)):

            # Step 3: Skip duplicate values for index i
            # If current value is same as previous, skip it
            # This avoids duplicate triplets starting with same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 4: Initialize two pointers
            # left starts just after i
            # right starts at the end
            left, right = i + 1, len(nums) - 1

            # Step 5: Use two-pointer approach
            # Continue until pointers meet
            while left < right:

                # Calculate sum of current triplet
                total = nums[i] + nums[left] + nums[right]

                # Case 1: Found a valid triplet
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Step 6: Skip duplicates for left pointer
                    # If next value is same, skip it
                    # This avoids repeating same triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Step 7: Skip duplicates for right pointer
                    # Same logic as left
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers inward after finding valid triplet
                    left += 1
                    right -= 1

                # Case 2: Sum is too small → increase it
                elif total < 0:
                    # Move left pointer right to increase sum
                    left += 1

                # Case 3: Sum is too large → decrease it
                else:
                    # Move right pointer left to decrease sum
                    right -= 1

        # Step 8: Return all unique triplets
        return result