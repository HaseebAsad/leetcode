class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count = {}

        # Build a dictionary with the count of S1/S2 words, returning 0 if the word is not in the dictionary.
        # e.g. 1 maps to ("this", "that"), 2 maps to ("there"), 3 maps to ... etc.
        for word in s1.split() + s2.split():
            word_count[word] = word_count.get(word, 0) + 1
        
        # Create a new list of ALL words with count == 1 in the dictionary.
        return [word for word, count in word_count.items() if count == 1]
