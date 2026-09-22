from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        target = Counter(t)
        window = defaultdict(int)

        required = len(target)
        have = 0

        left = 0
        best_length = float("inf")
        best_left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left

                left_char = s[left]
                window[left_char] -= 1

                if (
                    left_char in target
                    and window[left_char] < target[left_char]
                ):
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]