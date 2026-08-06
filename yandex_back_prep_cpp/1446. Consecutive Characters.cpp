#include <limits>
#include <algorithm>

class Solution
{
public:
    int maxPower(string s)
    {

        if (s.size() == 1)
        {
            return 1;
        }

        int max_len = std::numeric_limits<int>::lowest();

        int l = 0;
        int r = 0;

        while (r < s.size() - 1)
        {
            while (r < s.size() - 1 && s[r] == s[r + 1])
            {
                r++;
            }
            max_len = std::max(max_len, r - l + 1);
            r++;
            l = r;
        }

        return max_len;
    }
};