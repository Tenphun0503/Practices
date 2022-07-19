"""
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character.
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


def characterReplacement(s, k):
    l = 0
    c_frequency = {}
    longest_str_len = 0
    for r in range(len(s)):

        if not s[r] in c_frequency:
            c_frequency[s[r]] = 0
        c_frequency[s[r]] += 1

        # Replacements cost = cells count between left and right - highest frequency
        cells_count = r - l + 1
        if cells_count - max(c_frequency.values()) <= k:
            longest_str_len = max(longest_str_len, cells_count)

        else:
            c_frequency[s[l]] -= 1
            if not c_frequency[s[l]]:
                c_frequency.pop(s[l])
            l += 1

    return longest_str_len



s = 'ABAB'
k = 2

# s = "AABABBA"
# k = 1
print(characterReplacement(s, k))