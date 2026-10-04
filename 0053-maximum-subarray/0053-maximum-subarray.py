class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum = 0
        currentsum = 0
        for i in range(len(nums)):
            currentsum += nums[i]
            if currentsum < 0:
                currentsum = 0
            else:
                if currentsum > maxsum:
                    maxsum = currentsum
        if maxsum == 0:
            maxsum = max(nums)
        return maxsum
        