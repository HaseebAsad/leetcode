class Solution:
    def findComplement(self, num: int) -> int:
        x = list(bin(num)[2:])
        y = ''.join(map(str, [0 if i == '1' else 1 for i in x]))
        return int(y, 2)
