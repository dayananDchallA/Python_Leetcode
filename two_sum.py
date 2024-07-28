'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
-----------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
-----------
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
-----------
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
-----------
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
'''
from typing import List

class Solution:
    def two_sum(self,nums: List[int], target: int) -> List[int]:
        # Initialize the two pointers
        seen = {}

        for i, num in enumerate(nums):
            diff = target-num 
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

        return  []    
    
if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    print(sol.two_sum(nums, target))
    nums = [3,2,4]
    target = 6
    print(sol.two_sum(nums, target))
    nums = [3,3]
    target = 6
    print(sol.two_sum(nums, target))
    target = 11
    nums = [1,2,3,4,13]
    print(sol.two_sum(nums, target))