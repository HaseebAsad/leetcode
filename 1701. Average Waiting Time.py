class Solution(object):
    
    def __init__(self):

        self.currentTime = 0
        self.totalWaitTime = 0

    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        # customers = sorted(customers, key=lambda x: (x[0]))
        self.currentTime = self.currentTime = customers[0][0]
        for i in range(0,len(customers)):
            arrivalTime = customers[i][0]
            if arrivalTime < self.currentTime:
                waitTime = self.currentTime - arrivalTime # Time customer had to wait to be served
                self.totalWaitTime += customers[i][1] + waitTime
            else:
                self.totalWaitTime += customers[i][1]
            self.currentTime += customers[i][1]
        return (self.totalWaitTime/len(customers))
