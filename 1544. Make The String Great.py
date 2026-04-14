class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for str in s:
            if stack and stack[-1] != str and stack[-1].lower() == str.lower():
                stack.pop()

                #                 Step-by-step Breakdown
                # 1️⃣ stack
                # if stack

                # 👉 Checks that stack is not empty

                # Why?

                # Because we use stack[-1] (last element)
                # If empty → error
                # 2️⃣ stack[-1] != ch

                # 👉 Ensures characters are not exactly the same

                # Example:

                # 'a' vs 'a' → same → ❌ don’t remove
                # 'a' vs 'A' → different → ✅ possible removal
                # 3️⃣ stack[-1].lower() == ch.lower()

                # 👉 Checks if both are same letter ignoring case

                # Example:

                # 'a' and 'A' → both become 'a' ✅
                # 'b' and 'B' → both become 'b' ✅
                # 'a' and 'b' → ❌
                # 🔥 Combine all conditions

                # So the full condition means:

                # “If last character exists AND
                # current character is different BUT
                # both are same letter ignoring case”

                # 👉 Then it's a bad pair → remove it
            
            else:
                stack.append(str)

        return "".join(stack)