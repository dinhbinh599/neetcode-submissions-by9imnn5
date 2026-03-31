public class Solution {
    public int MaxArea(int[] heights) {
        var L = 0;
        var R = heights.Length - 1;

        var maxAmount = 0;

        while (L < R)
        {
            var height = Math.Min(heights[L], heights[R]);
            var amount = height * (R - L);
            if (amount > maxAmount)
            {
                maxAmount = amount;
            }

            if (heights[L] < heights[R]){
                L++;
            }
            else {
                R--;
            }
        }

        return maxAmount;
    }
}
