#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jul  9 17:57:26 2022

@author: miaosenzhou
"""

"""
Given a string s, find the length of the longest substring 
without repeating characters.


Example:
    
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is 
a subsequence and not a substring.

"""

class Length_Of_Longest_Substring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Define the variabel 
        ans = 0
        n = len(s)
        compare = {}
        
        i = 0
        for j in range(len(s)):
                print ("analyisis:  "+ s[j])
                if s[j] in compare:
                    i = max(compare[s[j]],i)
                ans = max(ans, j-i+1)
                compare[s[j]] = j+1
        
        return ans