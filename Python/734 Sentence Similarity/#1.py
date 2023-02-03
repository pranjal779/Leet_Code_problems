class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pairs_dict = defaultdict(set)
        for pair in similarPairs:
            pairs_dict[pair[0]].add(pair[1])
            pairs_dict[pair[1]].add(pair[0])
        
        
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2 and word2 not in pairs_dict[word1]:           
                return False
            
        return True
