from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        target = Counter(s1)
        window = Counter(s2[:window_size])

        if window == target:
            return True

        for right in range(window_size, len(s2)):
            # Add the new right character
            window[s2[right]] += 1

            # Remove the old left character
            left = right - window_size
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            if window == target:
                return True
        return False
