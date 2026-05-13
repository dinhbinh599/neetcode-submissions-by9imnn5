public class Solution {
    public int Search(int[] nums, int target) {
        var L = 0;
        var R = nums.Length - 1;

        while (L <= R){
            int mid = L + (R - L) / 2;
            
            if (nums[mid] == target){
                return mid;
            }

            if (nums[mid] > target){
                R = mid - 1;
            }
            else 
            {
                L = mid + 1;
            }
        }
        return -1;
    }
}
