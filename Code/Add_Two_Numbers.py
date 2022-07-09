#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 9 01:03:56 2022

@author: miaosenzhou
"""

"""
You are given two non-empty linked lists representing 
two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains 
a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

eg:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Add_Two_Numbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        add = 0
        carry = 0
        result = ListNode(0)
        ans = result
        
        while (l1!=None or l2!=None):
            if (l1 !=None):
                num1 = l1.val 
            else: num1 = 0
            
            if (l2 !=None):
                num2=l2.val 
            else: num2 = 0
            
            add = num1+num2+carry
            carry = int (add/10)
            
            ans.next = ListNode(add % 10)
            ans = ans.next
            
            if (l1 !=None):
                l1= l1.next
            if (l2 !=None):
                l2= l2.next
        if (carry>0):
            ans.next = ListNode(carry)
        
       
        return result.next
