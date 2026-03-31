public class Solution {
    public bool IsPalindrome(string s) {
        var L = 0;
        var R = s.Length - 1;

        while (L < R){
            if (!char.IsLetterOrDigit(s[L])){
                L++;
                continue;
            }
            if (!char.IsLetterOrDigit(s[R])){
                R--;
                continue;
            }
            if (char.ToLower(s[L]) != char.ToLower(s[R])){
                return false;
            }
            L++;
            R--;
        }
        return true;
    }
}
