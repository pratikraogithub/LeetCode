class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # variable for storing the result
        result = 0

        for num in nums:
            # XOR operation
            result = result ^ num

        return result
    
    # result = result ^ num
    # XOR Operation
    # 4  ....  1 0 0
    # 1  ....  0 0 1
    # 2  ....  0 1 0
    # 1  ....  0 0 1
    # 2  ....  0 1 0
    # result.  1 0 0
    # if we do addition of this the result will be 4


#     In XOR, we do NOT take carry

# But that sentence alone is a bit abstract — let’s make it super clear visually.

# 🧠 What does “no carry” actually mean?

# When we work with numbers, we do it bit by bit (binary).

# 🔴 Normal Addition (HAS carry)

# Example: 1 + 1

#   1
# + 1
# ----
#  10   ← carry generated

# 👉 Result becomes 2

# 🟢 XOR (NO carry)

# Same example: 1 ^ 1

#   1
# ^ 1
# ----
#   0   ← NO carry, just compare

# 👉 Result = 0

# 🔍 Side-by-side comparison
# Example: 3 + 1
# 3 = 011
# 1 = 001

#  011
# +001
# -----
#  100  ← carry happens

# 👉 Answer = 4

# XOR: 3 ^ 1
#  011
# ^001
# -----
#  010  ← no carry

# 👉 Answer = 2

# 🧠 So what XOR really does

# Instead of adding, it just checks each bit:

# Bit A	Bit B	Result
# same	same	0
# different	different	1

# 👉 No carry, no borrowing, nothing extra