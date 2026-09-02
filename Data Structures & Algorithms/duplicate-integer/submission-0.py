class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = {}
        for item in nums:
            if item not in mapper:
                mapper[item] = 1
            else:
                return True
        return False
