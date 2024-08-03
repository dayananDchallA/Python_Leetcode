'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
-------------
Input: s = "()"
Output: true

Example 2:
-------------
Input: s = "()[]{}"
Output: true

Example 3:
-------------
Input: s = "(]"
Output: false
 
Constraints:
-------------
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c not in mapping:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()

        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    print(sol.isValid(s))
    sol = Solution()
    s = "(]"
    print(sol.isValid(s))
    sol = Solution()
    s = "()"
    print(sol.isValid(s))
        