class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_prod = [1] * n
        prefix_prod[0] = nums[0]

        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i - 1] * nums[i]

        suffix_prod = [1] * n
        suffix_prod[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_prod[i] = suffix_prod[i + 1] * nums[i]

        result = [1] * n

        for i in range(n):
            if i == 0:
                result[i] = suffix_prod[i + 1]
            elif i == n - 1:
                result[i] = prefix_prod[i - 1]
            else:
                result[i] = prefix_prod[i - 1] * suffix_prod[i + 1]

        return result
