class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Use sorted with zip to sort by heights in descending order
        sorted_names = [name for name, _ in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]
        return sorted_names
