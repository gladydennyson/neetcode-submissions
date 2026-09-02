class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = ''
        ans = 0
        left = 0
        for right in range(len(s)):
            window += s[right]
            while window.count(s[right]) > 1: # update left until window is valid again
                window = window[1:]
                left += 1
            ans = max(ans, len(window))        # window is guaranteed to be valid here
        return ans