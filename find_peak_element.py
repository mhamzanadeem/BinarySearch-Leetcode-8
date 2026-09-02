from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid is in an increasing slope, peak is to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If mid is in a decreasing slope, peak is to the left (including mid)
            else:
                right = mid
        
        # left == right, pointing to a peak
        return left