from tokenize import group


def groupAnagrams(strs):
    # Key Idea: All anagrams are the same when sorted alphabetically.
    wordDict = {}
    result = []
    for i, val in enumerate(strs):
        sortedVal = ''.join(sorted(val)) #transform word into sorted version

        if sortedVal in wordDict: #check if the anagram exists in dict
            wordDict[sortedVal].append(val) #append if it does.

        else:
            wordDict[sortedVal] = [val] #add sorted anagram if it doesn't exist
    for i in wordDict.keys(): # combine the results.
        result.append(wordDict[i])
    return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))