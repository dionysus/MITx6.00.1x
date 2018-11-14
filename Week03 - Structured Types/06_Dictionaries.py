def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    total = 0
    for each in aDict.keys():
        total += len(aDict[each])
    
    return total

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxNum = 0
    maxKey = ''
    
    for each in aDict.keys():
        if len(aDict[each]) > maxNum:
            maxNum = len(aDict[each])
            maxKey = each
    
    return maxKey