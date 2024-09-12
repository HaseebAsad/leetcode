class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed) # Sets are O(1) complexity for lookup instead of O(n) for lists
        return sum(all(char in allowed_set for char in word) for word in words)
# All returns boolean True if all elements in the iterable are truthy
