class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(
                nums[i],                 # start a new subarray
                current_sum + nums[i]    # continue existing subarray
            )

            max_sum = max(max_sum, current_sum)

        return max_sum