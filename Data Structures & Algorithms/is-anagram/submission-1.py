class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapper = {}
        for char in s:
            if char in mapper:
                mapper[char] += 1
            else:
                mapper[char] = 1
        
        for char in t:
            if char in mapper and mapper[char] > 1:
                mapper[char] -= 1
            elif char in mapper and mapper[char] == 1:
                del mapper[char]
            else:
                return False
        return True
