class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                w1, w2 = words[i], words[j]
                L = len(w1)
                if w1 == w2[:L] and w1 == w2[-L:]:
                    res += 1
        
        return res
        
