class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            curSet, subSet = [], []
            self.helper2(0, nums, curSet, subSet)
            return subSet

    def helper2(self, i, nums, curSet, subSet):
        if i >= len(nums):
            subSet.append(curSet.copy())
            return

        curSet.append(nums[i])
        self.helper2(i + 1, nums, curSet, subSet)
        curSet.pop()
        
        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        self.helper2(i + 1, nums, curSet, subSet)  