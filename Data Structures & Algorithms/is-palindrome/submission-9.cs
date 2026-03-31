public class Solution {
    public bool IsPalindrome(string s) {
        var L = 0;
        var R = s.Length - 1;

        while (L < R){
            if (!AlphaNum(s[L])){
                L++;
                continue;
            }
            if (!AlphaNum(s[R])){
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
    public bool AlphaNum(char c){
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
}
