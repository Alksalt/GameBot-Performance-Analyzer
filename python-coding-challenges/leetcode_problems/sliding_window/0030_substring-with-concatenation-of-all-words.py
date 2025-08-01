"""
Problem: 0030. Substring with Concatenation of All Words
Link: https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Description:
    Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once.

Approach:
    Use a sliding window and hash maps to count word occurrences and match all words.

Time Complexity: O(N * M * L)
Space Complexity: O(M * L)
"""

from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not words:
            return []

        len_s = len(s)
        len_one_word = len(words[0])
        words_dict = Counter(words)
        result = []
        total_len = len(words) * len_one_word

        for start in range(len_s - total_len + 1):
            window_counts = Counter()

            for i in range(len(words)):
                start_chunk = start + i * len_one_word
                end_chunk = start_chunk + len_one_word

                if s[start_chunk:end_chunk] not in words_dict:
                    break

                window_counts[s[start_chunk:end_chunk]] += 1

                if window_counts[s[start_chunk:end_chunk]] > words_dict[s[start_chunk:end_chunk]]:
                    break
            else:
                result.append(start)

        return result

sol = Solution()

print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))            # Expected: [0, 9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # Expected: []
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # Expected: [6,9,12]
print(sol.findSubstring("aaaaaa", ["aa","aa","aa"]))                     # Expected: [0]
print(sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])) # Expected: [13]
print(sol.findSubstring("abababab", ["ab","ab","ab"]))                   # Expected: [0,2]