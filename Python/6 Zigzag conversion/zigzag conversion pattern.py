class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1: return s

		res = ""
		for r in range(numRows):
			res += s[i]
			if(r > 0 and r < numRows -1 and
				i + increment - 2 * r < lens(s)):
				res += s(i + increment -2 * r)
		return res
