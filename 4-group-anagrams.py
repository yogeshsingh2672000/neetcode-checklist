strs = ["eat","tea","tan","ate","nat","bat"] # test case 1
# strs = [""] # test case 2
# strs = ["a"] # test case 3

def groupAnagrams(strs):
    hashmap = {}
    for ele in strs:
        temp = 0
        for char in ele:
            temp += ord(char)
        
        if temp not in hashmap:
            hashmap[temp] = [ele]
        else:
            hashmap[temp].append(ele)
    return list(hashmap.values())

print(groupAnagrams(strs))
# Time Complexity = O(n)