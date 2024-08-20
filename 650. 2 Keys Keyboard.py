class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        sum_of_prime_factors = 0
        while (n%2 == 0):
            sum_of_prime_factors += 2
            n //= 2
        # n is now odd. Test odd numbers until n has been fully factored. Use sqrt of n as upper bound.
        limit = int(math.sqrt(n)) + 1
        for i in range(3,limit,2):
            while n % i== 0:
                sum_of_prime_factors += i
                n //= i
        # If we finish on a number (must be prime) greater than 2, add it.
        if n > 2:
            sum_of_prime_factors += n
        return sum_of_prime_factors
