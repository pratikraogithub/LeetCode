class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Step 1: Sort the array
        # This helps in:
        # 1. Using two-pointer technique
        # 2. Skipping duplicates easily
        nums.sort()

        result = []   # This will store all unique quadruplets
        n = len(nums)

        # Step 2: First loop → Fix the first number (nums[i])
        for i in range(n):

            # Skip duplicate values for i
            # If current value is same as previous, we already processed it
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Second loop → Fix the second number (nums[j])
            for j in range(i + 1, n):

                # Skip duplicate values for j
                # Same idea: avoid repeating same pair (i, j)
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Step 4: Two pointers for remaining two numbers
                left, right = j + 1, n - 1

                # Step 5: Find pairs using two-pointer approach
                while left < right:

                    # Calculate total sum of 4 elements
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # Case 1: Found a valid quadruplet
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicate values for left pointer
                        # This ensures we don't add same quadruplet again
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate values for right pointer
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move both pointers after finding valid result
                        left += 1
                        right -= 1

                    # Case 2: Sum is too large → decrease it
                    elif total > target:
                        right -= 1   # Move right pointer left to reduce sum

                    # Case 3: Sum is too small → increase it
                    else:
                        left += 1    # Move left pointer right to increase sum

        # Step 6: Return all unique quadruplets
        return result