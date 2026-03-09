from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i-k]    # remove element leaving window
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k