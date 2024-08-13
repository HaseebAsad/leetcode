class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # contiguous -> must touch
        counter = 0 # Total number of subarrays
        cnt = 0
        for i in range(len(nums)):
            cnt = nums[i]
            if (cnt == k):
                    counter +=1
            for j in range(i+1, len(nums),1):
                cnt += nums[j]
                if (cnt == k):
                    counter +=1
            cnt = 0 #reset
        return counter
