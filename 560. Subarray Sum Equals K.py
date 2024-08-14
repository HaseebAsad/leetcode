class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}  # Initialize with 0.
        
        for num in nums:
            current_sum += num
            
            # KEY IDEA: Check if there is a prefix sum that equals current_sum - k. This uses the hint and reduces the number of operations.
            # It uses the dictionary and the current sum - prefix_sums to check for subarrays!!!!!! sum(i,j) = sum(0,j)-sum(0,i); i, j indexes.
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]

            if current_sum in prefix_sums:
                prefix_sums[current_sum] += 1
            else:
                prefix_sums[current_sum] = 1 # Add to dictionary the current sum with frequency of 1.
        
        return count
