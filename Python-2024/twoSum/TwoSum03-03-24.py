class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptyList_for_req_num = {}
        for i, num in enumerate(nums):
            for_req_num = target - nums[i]
            if for_req_num in emptyList_for_req_num:
                return [emptyList_for_req_num[for_req_num], i]
            emptyList_for_req_num[nums[i]] = i

        return []

