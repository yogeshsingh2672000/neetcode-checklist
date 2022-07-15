s, t = "anagram", "nagaram" # test case 1
# s, t = "rat", "car" # test case 2

def isAnagram(s, t):
    shash = {}
    thash = {}
    for i in range(len(s)):
        shash[s[i]] = 1 + shash.get(s[i], 0)
        thash[t[i]] = 1 + thash.get(t[i], 0)
    if shash == thash:
        return True
    else:
        return False

print(isAnagram(s, t))