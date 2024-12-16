class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptyDict_for_req_num = {}
        for i, num in enumerate(nums):
            for_req_num = target - nums[i]
            if for_req_num in emptyDict_for_req_num:
                return [emptyDict_for_req_num[for_req_num], i]
            emptyDict_for_req_num[nums[i]] = i

        return []
