from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        # Initialize count to track the number of times the
        # current number is less than the previous number in the list
        decrease_count = 0
      
        # Iterate over the list of numbers along with the index
        for i, value in enumerate(nums):
            # If the current value is less than the previous value (circularly),
            # we increment the decrease_count.
            # nums[i - 1] accesses the previous element since Python supports
            # negative indexing, for the first element it will compare with the last element
            if nums[i - 1] > value:
                decrease_count += 1
      
        # The array is considered sorted and rotated at most once if there's zero or one decrease
        return decrease_count <= 1
