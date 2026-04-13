class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0] * len(nums)
        print(suffix)
        for i in range(len(nums)):
            if len(prefix) == 0:
                prefix.append(1)
                continue
            target = nums[i-1] * prefix[i-1]
            prefix.append(target)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) -1:
                print(i)
                suffix[i] = 1
                continue
            target = nums[i+1] * suffix[i+1]
            suffix[i] = target

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res