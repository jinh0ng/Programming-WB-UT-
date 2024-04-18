# File: MyStringFunctions.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date: 03/16/24
# Description of Program:   This assignment defines string manipulation functions without using built-in string methods


def myAppend(s, ch):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount(s, ch):
    # Return the number of times character ch appears
    # in s.
    count = 0
    for char in s:
        if char == ch:
            count += 1
    return count

def myExtend(s1, s2):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1 + s2

def myMin(s):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    if len(s) == 0:
        print("Empty string: no min value")
        return None
    else:
        min_char = s[0]
        for char in s:
            if char < min_char:
                min_char = char
        return min_char

def myInsert(s, i, ch):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    if i > len(s):
        print("Invalid index")
        return None
    else:
        return s[:i] + ch + s[i:]

def myPop(s, i):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    if i >= len(s):
        print("Invalid index")
        return s, None
    else:
        return s[:i] + s[i+1:], s[i]

def myFind(s, ch):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1

def myRFind(s, ch):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    index = -1
    for i in range(len(s)):
        if s[i] == ch:
            index = i
    return index

def myRemove(s, ch):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    index = myFind(s, ch)
    if index == -1:
        return s
    else:
        return s[:index] + s[index+1:]

def myRemoveAll(s, ch):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    new_s = ""
    for char in s:
        if char != ch:
            new_s += char
    return new_s

def myReverse(s):
    # Return a new string like s but with the characters
    # in the reverse order.  For this one, don't use slicing.
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s

def isPalindrome(s):
    # Return a Boolean indicating whether the input string s
    # reads the same forward or backward.
    return s == myReverse(s)
