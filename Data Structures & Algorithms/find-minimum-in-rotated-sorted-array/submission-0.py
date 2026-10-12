class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l = 0 
        r = len(nums) - 1
        minElem = 0

        while l < r:
            mid = (l+r) // 2
            
            # item in second half
            if nums[mid] > nums[r]:
                l = mid + 1
            # item in first half or the mid itself
            else:
                r = mid 
            
        return nums[l]