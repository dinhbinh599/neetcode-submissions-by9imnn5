class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []
        for i in range(len(nums)):
            if not prefixSum:
                prefixSum.append(0)
            else:
                prefixSum.append(prefixSum[i-1] + nums[i-1])

        postfixSum = []
        lastSum = 0
        for i in range(len(nums) - 1, -1, -1):
            if not postfixSum:
                postfixSum.append(0)
            else:
                postfixSum.append(lastSum + nums[i+1])
                lastSum = lastSum + nums[i+1]

        print(postfixSum)
        print(prefixSum)

        for i in range(len(nums)):
            if prefixSum[i] == postfixSum[len(nums) -1 - i]:
                return i
        
        return -1
            



