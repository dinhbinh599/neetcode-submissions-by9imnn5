class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, val in enumerate(nums):
            if target - val in my_dict and my_dict[target-val] != index:
                return [my_dict[target-val], index]
            my_dict[val] = index
        return []