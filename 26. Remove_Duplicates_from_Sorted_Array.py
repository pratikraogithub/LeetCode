class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

         # Edge case: if array is empty
        if not nums:
            return 0
        
        # 'i' points to last unique element
        i = 0

        # 'j' scans the array
        for j in range(1, len(nums)):

            # If new unique element found
            if nums[j] != nums[i]:
                i += 1              # Move position for next unique element

                nums[i] = nums[j]   # Place new unique element


        # Return count of unique elements

        # nums = [1]
        # i = 0
        # 👉 Unique elements = 1
        # return i + 1 = 1
        return i + 1
    


# Step-by-Step Dry Run
# Input:
# nums = [1, 1, 2, 2, 3]
# Initial:
# i = 0
# nums = [1, 1, 2, 2, 3]
# j = 1:
# nums[1] == nums[0] → skip
# j = 2:
# nums[2] != nums[0] → new element
# i = 1
# nums = [1, 2, 2, 2, 3]
# j = 3:
# duplicate → skip
# j = 4:
# new element
# i = 2
# nums = [1, 2, 3, 2, 3]
# ✅ Final Output
# k = 3
# nums = [1, 2, 3, _, _]