class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.sort()
        k = 0
        while k < len(nums) - 1:
            if nums[k] == nums[k+1]:
                nums.pop(k+1)
            else:
                k += 1
        return len(nums)

