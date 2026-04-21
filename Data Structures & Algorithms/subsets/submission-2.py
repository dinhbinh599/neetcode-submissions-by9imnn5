class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            subsets, curSet = [], []
            self.helper2(0, nums, curSet, subsets)
            return subsets

    def helper2(self, i, nums, curSet, subsets):
        if i >= len(nums):
            subsets.append(curSet.copy())
            return

        # decision to include nums[i]
        curSet.append(nums[i])
        self.helper2(i + 1, nums, curSet, subsets)
        curSet.pop()

        # decision NOT to include nums[i]
        while i +1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper2(i + 1, nums, curSet, subsets)