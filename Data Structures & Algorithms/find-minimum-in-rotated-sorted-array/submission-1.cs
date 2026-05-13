public class Solution {
    public int FindMin(int[] nums) {
        var min = 1000;
        foreach (var num in nums){
            min = Math.Min(min, num);
        }

        return min;
    }
}
