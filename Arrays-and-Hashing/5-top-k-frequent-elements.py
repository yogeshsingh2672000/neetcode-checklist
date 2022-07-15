from cgitb import reset


# nums, k = [1,1,1,2,2,3], 2
nums, k = [1], 1

hashmap = {}
for i in nums:
    hashmap[i] = 1 + hashmap.get(i, 0)

res = [] # output

for j in hashmap.values:
    if hashmap[j] >= k:
        res.append(j)

print(res)
