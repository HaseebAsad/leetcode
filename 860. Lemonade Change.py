class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # hash map solution. count the numbers of 5s, 10s and 20s we have.
        # we know that if a 5 is paid, no change and add 5 to the hashmap
        # if 10 is paid, take one 5 away from the hashmap, and add a 10.
        # if 20 is paid, take either three 5s away from the hashmap. If this fails, try one 10 and one 5. Then, add 20 to the hashmap (not really necessary unless someone pays over 20, which they cant.)
        # so keep running totals of 5s or 10s. Hashmap may be overkill.
