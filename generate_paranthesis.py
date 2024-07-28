'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
-----------
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
-----------
Input: n = 1
Output: ["()"]
 
Constraints:
-----------
1 <= n <= 8
'''

from typing import List

class Solution:
    def generate_parent(self, n: int) -> List[str]:
        sol = []
        ans = []

        def backtrack(num_open, num_close):
            if num_open == num_close == n:
                ans.append("".join(sol))
                return
            
            if num_open < n:
                sol.append("(")
                backtrack(num_open+1, num_close)
                sol.pop()
            
            if num_close <  num_open:
                sol.append(")")
                backtrack(num_open, num_close+1)
                sol.pop()

        backtrack(0, 0)
        return ans
    
if __name__ == "__main__":
        sol = Solution()
        n = 3
        print(sol.generate_parent(n))
        n = 1
        print(sol.generate_parent(n))