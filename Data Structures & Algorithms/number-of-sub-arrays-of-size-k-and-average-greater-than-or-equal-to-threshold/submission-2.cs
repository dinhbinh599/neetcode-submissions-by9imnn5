public class Solution {
    public int NumOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
        var kMinusOne = k-1;
        int currSum = arr[..kMinusOne].Sum();

        for (int l = 0; l <= arr.Length - k; l++){
            currSum += arr[l + k - 1];
            if (currSum / k >= threshold){
                count++;
            }
            currSum -= arr[l];
        }

        return count;
    }
}