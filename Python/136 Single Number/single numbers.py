class Solution:
    def SingleNumber(self, nums: list[int]) -> int:
	res = 0  # n ^ 0 = n; ^ = xor
	for n in nums:
	    res = n ^ res
	return res
