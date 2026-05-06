class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L = i + 1
            R = len(nums) - 1

            while L < R:

                if nums[i] + nums[L] + nums[R] == 0:
                    res.add((nums[i], nums[L], nums[R]))
                    L+=1
                    R-=1
                elif nums[i] + nums[L] + nums[R] < 0:
                    L+=1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R-=1

        return list(res)
