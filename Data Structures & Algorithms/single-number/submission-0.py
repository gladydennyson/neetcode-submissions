class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numset = set()

        for num in nums:
            if num not in numset:
                numset.add(num)
            else:
                numset.remove(num)
            
        return list(numset)[0]