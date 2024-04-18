# File: MyListFunctions.py
# Student: Yejin Hong
# UT EID: yh25386   
# Course Name: CS303E
# 
# Date: 03/25/24
# Description of Program: This assignment involves defining functions to manipulate lists, such as adding, extending, finding maximums, counting occurrences, inserting, popping, finding indices, reversing, and removing elements. 

def myAppend( lst, x ):
    # Return a new list that is like lst but with 
    # the element x at the right end
    return lst + [x]

def myExtend( lst1, lst2 ):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in the order
    # given.
    result = []
    for elem in lst1:
        result.append(elem)
    for elem in lst2:
        result.append(elem)
    return result

def myMax( lst ):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.
    if not lst:
        print("Empty list: no max value")
        return None
    max_val = lst[0]
    for val in lst[1:]:
        if val > max_val:
            max_val = val
    return max_val

def mySum( lst ):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    total = 0
    for val in lst:
        total += val
    return total

def myCount( lst, x ):
    # Return the number of times element x appears
    # in lst.
    count = 0
    for val in lst:
        if val == x:
            count += 1
    return count


def myInsert( lst, i, x ):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and 
    # return None.
    if i < 0 or i > len(lst):
        print("Invalid index")
        return None
    result = lst[:i] + [x] + lst[i:]
    return result

def myPop( lst, i ):
    # Return two results: 
    # 1. a new list that is like lst but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    if i < 0 or i >= len(lst):
        print("Invalid index")
        return lst, None
    removed_value = lst.pop(i)
    return lst, removed_value    

def myFind( lst, x ):
    # Return the index of the first (leftmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    for i, val in enumerate(lst):
        if val == x:
            return i
    return -1    

def myRFind( lst, x ):
    # Return the index of the last (rightmost) occurrence of 
    # x in lst, if any.  Return -1 if ch does not occur in lst.
    last_index = -1
    for i, val in enumerate(lst):
        if val == x:
            last_index = i
    return last_index

def myFindAll( lst, x ):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    indices = []
    for i, val in enumerate(lst):
        if val == x:
            indices.append(i)
    return indices

def myReverse( lst ):
    # Return a new list like lst but with the elements
    # in the reverse order. 
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

def myRemove( lst, x ):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    for i, val in enumerate(lst):
        if val == x:
            return lst[:i] + lst[i+1:]
    return lst

def myRemoveAll( lst, x ):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    result = []
    for val in lst:
        if val != x:
            result.append(val)
    return result

# Don't use slicing for this one:
def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves.
    pass