class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for i in range(len(nums)):
            if i == 0:
                self.prefix.append(nums[i])
            else:
                self.prefix.append(nums[i] + self.prefix[i-1])
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        leftVal = 0
        if left != 0:
            leftVal = self.prefix[left-1]
        return self.prefix[right] - leftVal


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)