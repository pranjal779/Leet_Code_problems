class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if r - l > 1:
                res += len(set(s[l + 1 : r]))
        return res
        
        # res = set() # (mid_c, outer_c)
        # left = set()
        # right = Counter(s)

        # for m in s:
        #     right[m] -= 1
        #     for c in left:
        #         if right[c] > 0:
        #             res.add((m, c))
        #         left.add(m)

        # return len(res)
