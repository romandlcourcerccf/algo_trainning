class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int i = 0;
        vector<char> prefix;

        vector<int> lens;
        for (auto s: strs) {
            lens.push_back(s.size());
        }

        int min_size = *min_element(lens.begin(), lens.end());

        for (int i=0; i<min_size; i++) {
            set<char> c;
            for (auto s: strs){
                c.insert(s[i]);
            }
            if (c.size() == 1) {
                prefix.push_back(*(c.begin()));
            } else {
                break;
            }

        }
 
        return string(prefix.begin(), prefix.end());

    }
};