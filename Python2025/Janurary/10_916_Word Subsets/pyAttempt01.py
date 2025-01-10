class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Create a counter to store the maximum frequency of each character 
        # across all words in words2
        max_freq_counter = Counter()
        for word in words2:
            word_freq_counter = Counter(word)
            for char, freq in word_freq_counter.items():
                # Update the counter for each character to the maximum frequency
                max_freq_counter[char] = max(max_freq_counter[char], freq)
      
        # Initialize a list to keep all words from words1 that meet the criteria
        universal_words = []
        # Iterate through each word in words1 to check if it is a universal word
        for word in words1:
            word_freq_counter = Counter(word)
            # Check if word has at least as many of each character as needed
            is_universal = all(freq <= word_freq_counter[char] for char, freq in max_freq_counter.items())
            # If the word meets the criteria, add it to the universal words list
            if is_universal:
                universal_words.append(word)
      
        # Return the list of universal words
        return universal_words
