class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}  # character frequencies
        ans = 0
        left = 0

        for right in range(len(s)):
            # Append s[right] to window
            window[s[right]] = window.get(s[right], 0) + 1

            # Invalid when required replacements exceed k
            while (right - left + 1) - max(window.values()) > k:
                # Remove s[left] from window
                window[s[left]] -= 1
                left += 1

            # Window is valid here
            ans = max(ans, right - left + 1)

        return ans
  