class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # hash map solution. count the numbers of 5s, 10s and 20s we have.
        # we know that if a 5 is paid, no change and add 5 to the hashmap
        # if 10 is paid, take one 5 away from the hashmap, and add a 10.
        # if 20 is paid, take either three 5s away from the hashmap. If this fails, try one 10 and one 5. Then, add 20 to the hashmap (not really necessary unless someone pays over 20, which they cant.)
        # so keep running totals of 5s or 10s. Hashmap may be overkill.
        fives = 0
        tens = 0
        for bill in bills:
            print("bill to pay:",bill, " current fives:", fives, " current tens:", tens)
            if bill == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif bill == 20:
                if fives >= 1 and tens >= 1: #USE HIGHEST DENOMINATION FIRST!!!!
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
            else:  # bill == 5
                fives += 1
            print("change given")
        return True


# example of code with better runtime
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1
                five -= 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return "false"
        return "true"

s = Solution()
with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"{s.lemonadeChange(case)}\n")
exit(0)
