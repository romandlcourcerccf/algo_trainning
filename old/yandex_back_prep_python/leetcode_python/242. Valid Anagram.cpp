class Solution {
public:
    bool isAnagram(string s, string t) {
        
        map<char, int> counter1;
        map<char, int> counter2;

        for (auto c: s) {
            counter1[c] +=1;
        }

        for (auto c: t) {
            counter2[c] +=1;
        }

        return counter1 == counter2;