#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 01:03:56 2022

@author: miaosenzhou
"""

"""
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Examples: 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Function:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j and nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
            if len(ans) == 2 :
                break
        # return indices
        return ans



"""
#Given an array of integers nums and an integer target, return elements of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

#Examples: 
Input: nums = [2,7,11,15], target = 9
Output: [2,7]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [2,4]

Input: nums = [3,3], target = 6
Output: [3,3]
"""

class Function:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!= j and nums[i]+nums[j] == target:
                    ans.append(nums[i])
                    ans.append(nums[j])
            if len(ans) == 2 :
                break
        # return indices
        return ans

