class Solution:
    def maxAbsoluteSum(self, nums):
        curr_max = max_sum = 0
        curr_min = min_sum = 0
        for num in nums:
            curr_max = max(0, curr_max + num)
            max_sum = max(max_sum, curr_max)
            # Minimum subarray sum
            curr_min = min(0, curr_min + num)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))
