public class Solution {
    public int FindMin(int[] nums) {
        var min = int.MaxValue;
        foreach (var num in nums){
            min = Math.Min(min, num);
        }

        return min;
    }
}
