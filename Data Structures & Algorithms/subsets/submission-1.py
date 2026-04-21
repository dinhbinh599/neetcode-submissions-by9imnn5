class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []

            def backtrack(start, cur):
                res.append(cur.copy())

                for i in range(start, len(nums)):
                # 🚫 skip duplicates at same level
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    cur.append(nums[i])
                    backtrack(i + 1, cur)
                    cur.pop()

            backtrack(0, [])
            return res