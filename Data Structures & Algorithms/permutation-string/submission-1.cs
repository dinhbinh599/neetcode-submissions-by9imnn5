public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        var map1 = new Dictionary<char, int>();

        var k = s1.Length;

        for (var i = 0; i < s1.Length; i++){
            map1[s1[i]] = 1 + map1.GetValueOrDefault(s1[i], 0);
        }

        var map2 = new Dictionary<char, int>();
        for (var i = 0; i < s2.Length - k + 1; i++){
            if (i > 0){
                map2[s2[i-1]]--;
                if (map2[s2[i-1]] == 0){
                    map2.Remove(s2[i-1]);
                }
                map2[s2[i+k-1]] = 1 + map2.GetValueOrDefault(s2[i+k-1], 0);
                Console.WriteLine(string.Join(',', map2.Select(kvp => $"{kvp.Key}: {kvp.Value}")));
            }
            else
            {
                for(var y = i; y < i + k; y++)
                {
                    map2[s2[y]] = 1 + map2.GetValueOrDefault(s2[y], 0);
                }
            }

            if (IsPermunation(map1, map2)){
                return true;
            }
        }

        return false;
    }

    public bool IsPermunation(Dictionary<char,int> dict1, Dictionary<char,int> dict2){
        return dict1.Count == dict2.Count && !dict1.Except(dict2).Any();
    }
}
