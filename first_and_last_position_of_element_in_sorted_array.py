from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # Continue searching left for first occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return first
        
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # Continue searching right for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return last
        
        if not nums:
            return [-1, -1]
        
        first = findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        
        last = findLast(nums, target)
        return [first, last]