nums = [1,2,3,1] # test-case-1
#nums = [1,2,3,4] # test-case-2

def containsDuplicate(nums):
    hashmap = {}
    for i in nums:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            return True
    return False

print(containsDuplicate(nums))
# Time complexity = O(n)