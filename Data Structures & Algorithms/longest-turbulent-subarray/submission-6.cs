public class Solution {
    public int MaxTurbulenceSize(int[] arr) {
        var l = 0;
        var r = 1;
        var res = 1;
        var sign = "";

        while (r < arr.Length){
            if (arr[r-1] < arr[r] && sign != "<") {
                res = Math.Max(res, r - l + 1);
                r++;
                sign = "<";
            }
            else if (arr[r-1] > arr[r] && sign != ">"){
                res = Math.Max(res, r - l + 1);
                r++;
                sign = ">";
            }
            else {
                r = arr[r-1] == arr[r] ? r + 1 : r;
                l = r - 1;
                sign = "";
            }
        }

        return res;
    }
}