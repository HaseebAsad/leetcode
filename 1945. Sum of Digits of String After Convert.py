class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # list(s) to get a string as a list of characters. ord(x) - 96 for each x in list(s) will give the number.
        # need to make sure we treat each number as its own character: e.g. 23 as 2 and 3 instead of 23
        x = sum(int(digit) for char in s for digit in str(ord(char) - 96))
        for _ in range(k - 1):
            x = sum(int(digit) for digit in str(x))
        return x
