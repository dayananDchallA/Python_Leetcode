'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:
-------------
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
-------------
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
-------------
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:
-------------
1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

from typing import List

class Solution:
    def length_of_last_word(self, s: str) -> int:
        n = len(s)
        i = n-1

        while s[i] == ' ': i -= 1

        letter_count = 0
        for i in range(i+1):
            if s[i]!=' ':
                letter_count += 1
            else:
                letter_count = 0

        return letter_count
        
if __name__ == "__main__":
    sol = Solution()
    s = "Hello World"
    print(sol.length_of_last_word(s))
    s = "   fly me   to   the moon  "
    print(sol.length_of_last_word(s))
    s = "luffy is still joyboy"
    print(sol.length_of_last_word(s))   