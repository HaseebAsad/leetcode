class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Sort the numbers first by frequency (ascending) and then by value (descending)
        return sorted(nums, key=lambda x: (Counter(nums)[x], -x))
