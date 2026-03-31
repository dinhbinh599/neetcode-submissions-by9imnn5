public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> map = new HashSet<int>();
        foreach (var num in nums){
            if (map.Contains(num)){
                return true;
            }
            map.Add(num);
        }
        return false;
    }
}