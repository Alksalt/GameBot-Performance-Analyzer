from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            anagram_dict[tuple(sorted(word))].append(word)

        return list(anagram_dict.values())


    def groupAnagrams1(self, strs: list[str]) -> list[list[str]]:
        result = []
        d = {}
        idx = 0
        for word in strs:
            current_word = tuple(sorted(word))
            if current_word not in d:
                d[current_word] = idx
                result.append([word])
                idx += 1
            else:
                result[d[current_word]].append(word)
        return result

    from collections import defaultdict


    def groupAnagrams3(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
            anagram_dict[tuple(count)].append(word)

        return list(anagram_dict.values())


# Example input cases
strs1 = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]

# Usage setup
sol = Solution()
print(sol.groupAnagrams(strs1))  # Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
print(sol.groupAnagrams(strs2))  # Expected: [[""]]
print(sol.groupAnagrams(strs3))  # Expected: [["a"]]

