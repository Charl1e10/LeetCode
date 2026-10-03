class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            elif target < nums[i + 1] and target > nums[i]:
                return i + 1
        if nums[len(nums) - 1] < target:
            return len(nums)
        elif nums[len(nums) - 1] == target:
            return len(nums) - 1
        else:
            return 0    