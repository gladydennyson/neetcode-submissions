from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = Counter(nums)
        longest = 0
        for item in nums:
            if item - 1 not in counter:
                length = 1
                while item + length in counter:
                    length+= 1
                longest = max(length, longest)
        return longest


