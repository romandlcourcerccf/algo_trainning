#include <vector>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        
        int l = 0;
        int r = 0;
        while (r < chars.size()) {
            int _l = r;
            while (r < chars.size()-1 && chars[r] == chars[r+1]) {
                r +=1;
            }

            int ln = r-_l+1;
            chars[l] = chars[r];
            l +=1;

            if (ln > 1) {
                for (const char& c : to_string(ln)) {
                    chars[l] = static_cast<int>(c);
                    l +=1;
                }
            } 

            r+=1;

        }

        return l;
    }


};
