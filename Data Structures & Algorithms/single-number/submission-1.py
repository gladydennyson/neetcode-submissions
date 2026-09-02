class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cumulative_xor = 0
        for num in nums:
            cumulative_xor ^= num

        return(cumulative_xor)