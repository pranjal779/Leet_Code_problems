class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
	hashset = set()

	for n in nums:
	   if n in hashset:
	      return True
	   hashset.add(n)
	return False


# Time complexity is  O(n)
# Space complexicity is O(n)
