class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum = nums[0]
        currentsum = 0
        for i in range(len(nums)):
            currentsum += nums[i]
            if currentsum > maxsum:
                maxsum = currentsum
                
            if currentsum < 0:
                currentsum = 0
        return maxsum
        