class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for index , value in enumerate(nums):
            if target == value:
                return index 

            elif target != value and index == len(nums) -1:
                return -1  

            elif target != value:
                continue

            