class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # 'i' = index where we place the next valid (non-val) element
        # Think: "position to fill"
        i = 0

        # Loop through entire array using 'j'
        # 'j' = scanning pointer (explores every element)
        for j in range(len(nums)):

            # ----------------------------------------------------
            # DRY RUN EXAMPLE:
            # nums = [3, 2, 2, 3], val = 3
            #
            # j = 0 → nums[j] = 3 → skip
            # j = 1 → nums[j] = 2 → keep
            # j = 2 → nums[j] = 2 → keep
            # j = 3 → nums[j] = 3 → skip
            # ----------------------------------------------------

            # If current element is NOT equal to val
            if nums[j] != val:

                # Copy this element to position 'i'
                # (we overwrite unwanted elements)
                nums[i] = nums[j]

                # Move 'i' forward to next position
                i += 1

                # ------------------------------------------------
                # DRY RUN STEP-BY-STEP:
                #
                # Initial: nums = [3, 2, 2, 3], i = 0
                #
                # j = 1 → nums[j] = 2 (valid)
                # nums[0] = 2 → [2, 2, 2, 3]
                # i = 1
                #
                # j = 2 → nums[j] = 2 (valid)
                # nums[1] = 2 → [2, 2, 2, 3]
                # i = 2
                #
                # Final array (first i elements valid):
                # [2, 2, _, _]
                # ------------------------------------------------

        # 'i' is the number of elements NOT equal to val
        # So it represents the new length of array
        return i