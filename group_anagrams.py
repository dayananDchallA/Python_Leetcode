'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
----------
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
----------
Input: strs = [""]
Output: [[""]]

Example 3:
----------
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:
----------
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            s_sorted = sorted(s)
            key = tuple(s_sorted)

            if key not in ans:
                ans[key] = [s]
            else:
                ans[key].append(s)

        return ans.values()
    
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))
    sol = Solution()
    strs = [""]
    print(sol.groupAnagrams(strs))
    sol = Solution()
    strs = ["a"]
    print(sol.groupAnagrams(strs))