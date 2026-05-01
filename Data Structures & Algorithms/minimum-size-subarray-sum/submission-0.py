class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sum = 0
        res = float('inf')
        
        for r in range(len(nums)):
            sum+= nums[r]
            if sum >= target:
                res = min(res, r - l + 1)
                while sum - nums[l] >= target:
                    sum-= nums[l]
                    l+=1
                    res = min(res, r - l + 1)

        return 0 if res == float('inf') else int(res)