from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # If we can't determine which side is sorted due to duplicates
            if nums[left] == nums[mid]:
                left += 1
                continue
            
            # Left portion is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies in the left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Right portion is sorted
            else:
                # Check if target lies in the right sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False