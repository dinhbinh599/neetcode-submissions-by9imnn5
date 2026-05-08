public class Solution {
    public int CharacterReplacement(string s, int k) {
        var count = new Dictionary<char, int>();
        var res = 0;

        var l = 0;
        for (var r = 0; r < s.Length; r++){
            count[s[r]] = 1 + count.GetValueOrDefault(s[r], 0);

            while ((r-l+1) - count.Values.Max() > k){
                count[s[l]]--;
                l++;
            }

            res = Math.Max(res, r - l + 1);
        }
        return res;
    }
}
