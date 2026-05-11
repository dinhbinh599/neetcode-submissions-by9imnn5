public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var map = new Dictionary<int, int>();

        for (var i = 0; i < nums.Length; i++){
            if (map.ContainsKey(target - nums[i])){
                return new int[]{map[target-nums[i]], i};
            }
            map[nums[i]] = i;
        }

        return new int[]{0,0};
    }
}
