'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
-----------
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
-----------
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:
-----------
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
'''

class Solution:
    def last_occurence_index(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        n = len(haystack)
        m = len(needle)
        
        for i in range(n):
            j = 0
            for k in range(i, n):
                if haystack[k] == needle[j]:
                    j += 1
                else:
                    break
                if j == m:
                    return i
                
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    haystack = "sadbutsad"
    needle = "sad"
    print(sol.last_occurence_index(haystack, needle))
    haystack = "leetcode"
    needle = "leeto"
    print(sol.last_occurence_index(haystack, needle))
    
