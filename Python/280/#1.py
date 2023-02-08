class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        greater = False
        for i in range(len(nums)-1):
            if (greater and nums[i]<=nums[i+1]) or (not greater and nums[i]>=nums[i+1]):
                nums[i],nums[i+1]=nums[i+1],nums[i]
            greater = not greater


"""        for i in range(1, len(nums)):
            if ((i % 2 == 1 and nums[i] < nums[i - 1]) or
                (i % 2 == 0 and nums[i] > nums[i - 1])):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums
"""
# both solution is O(n)
