class Solution(object):

    def __init__(self):
        self.currentTime = 0
        self.totalWaitTime = 0

    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        self.currentTime = customers[0][0]
        for arrivalTime, cookTime in customers:
            if arrivalTime > self.currentTime:
                self.currentTime = arrivalTime
            self.totalWaitTime += self.currentTime + cookTime - arrivalTime
            self.currentTime += cookTime
        return self.totalWaitTime / len(customers)

"""
Potential improvements:
OOP is neither memory nor speed efficient. Consider not attaching attributes to the object to make more performant.
"""
