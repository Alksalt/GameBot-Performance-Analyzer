def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for word in strs[1:]:
            # if i is out of bounds or characters don't match, return what we have
            if i >= len(word) or word[i] != char:
                return prefix

        prefix += char

    return prefix

print(longestCommonPrefix(['longest', 'longestan', 'lonly', 'lol']))