class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = mx = 0
        seen = set()

        length = len(s)

        while j < length:
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                mx = max(mx, len(seen))

            else:
                seen.remove(s[i])
                i += 1
        return mx