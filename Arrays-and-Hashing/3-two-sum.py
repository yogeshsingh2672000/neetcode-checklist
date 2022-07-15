nums, target = [2,7,11,15], 9 # test case 1
nums, target  = [3,2,4], 6 # test case 2

def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in hashmap:
            return [hashmap[rem], i]
        else:
            hashmap[nums[i]] = i

    return

print(twoSum(nums, target))
# Time Complexity = O(n)