# Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ---Worked---
        # req_num_indecies_map = {}
        # n = len(nums)

        # for i in range(n):
        #     req_num = target - nums[i]
        #     if req_num in req_num_indecies_map:
        #         return [req_num_indecies_map[req_num], i]
        #     req_num_indecies_map[nums[i]] = i

        # return []
        # ---Worked---

        # wrong solution:
        # corrections done: at lines with for 'nums[i]' **
        req_num_map = {} # empty list to store the pair which will sum up to the target.
        for i, num in enumerate(nums): # i is pointing to index, num is the individual number in the list of nums
            req_num = target - nums[i] # ** # we now know which is other required number needed to reach the target
            if req_num in req_num_map: # checking if req_num is in req_num_map list ?
                return [req_num_map[req_num], i] # return the num, and req_num stored at req_num_map if found in the req_num_map, throught their index values
            req_num_map[nums[i]] = i # ** # save req_num at 0 index if i = 0, or the next one.

        # return a empty list [] if no pair is found
        return []


# Accepted
# Runtime: 53 ms
# Case 1
# Case 2
# Case 3
# Input
# nums =
# [2,7,11,15]
# target =
# 9
# Output
# [0,1]
# Expected
# [0,1]

# Wrong Answer
# Runtime: 78 ms
# Case 1
# Input
# nums =
# [2,7,11,15]
# target =
# 9
# Output
# []
# Expected
# [0,1]
#
# Case 2
# Input
# nums =
# [3,2,4]
# target =
# 6
# Output
# []
# Expected
# [1,2]
#
# Case 3
# Input
# nums =
# [3,3]
# target =
# 6
# Output
# [0,1]
# Expected
# [0,1]



# req_num_map = {}
#         for i in range(len(nums)):
#             req_num_map[nums[i] = i]

#         for i in range(len(nums)):
#             req_num_from_diff = target - nums[i]

#             if req_num_from_diff in req_num_map and req_num_map[req_num_from_diff] != 1:
#                 return[i, req_num_map[req_num_from_diff]]
