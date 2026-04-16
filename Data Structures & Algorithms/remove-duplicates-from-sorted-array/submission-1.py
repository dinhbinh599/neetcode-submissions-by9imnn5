class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        R = 0

        n = len(nums)

        print(n)

        while R < n:
            nums[L] = nums[R]
            while R < n and nums[L] == nums[R]:
                R+=1
            L+=1

        return L
        