# CS 303E Quiz 5D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: First Punctuation Locations
def firstPunctuationLocations(strings):
    result = {}
    for string in strings:
        punctuation_index = -1
        for index, char in enumerate(string):
            if char in ('.', '?', '!'):
                punctuation_index = index
                break
        result[string] = punctuation_index
    return result



# Problem 2: List of Odd Integers
def oddIntegers(nums):
    if not nums:
        return []
    
    if nums[0] % 2 != 0:
        return [nums[0]] + oddIntegers(nums[1:])
    else:
        return oddIntegers(nums[1:])



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    print(firstPunctuationLocations({'interesting... very interesting', 'is for me?', '!!!!!'}))
    print(firstPunctuationLocations({'Panic! At The Disco', '5! = 120', 'CS 303E'}))
    print(firstPunctuationLocations(set()))

    print(oddIntegers([38, 5, 10, -11, 20, 49, -19, 38, -11, 29, 0, -28]))
    print(oddIntegers([53, 51, -71, 22, -45, 20]))
    print(oddIntegers([8, -2, 6]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT