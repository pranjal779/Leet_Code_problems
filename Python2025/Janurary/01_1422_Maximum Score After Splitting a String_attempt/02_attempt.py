class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            right += 0 if s[i]=='0' else 1;
        for i in range(len(s)-1):
            left += 1 if s[i]=='0' else 0;
            right += 0 if s[i]=='0' else -1;
            right = max(0,right)
            ans = max(left+right,ans)
        return ans
