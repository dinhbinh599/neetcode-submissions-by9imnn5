public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (var i = 0; i < nums.Length; i++){
            var hash = target - nums[i];
            if (map.ContainsKey(hash)){
                return new int[]{map[hash], i};
            }
            map.Add(nums[i], i);
        }

        return new int[]{0, 0};
    }
}
