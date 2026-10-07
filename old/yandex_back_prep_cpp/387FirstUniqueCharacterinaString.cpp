#include <map>
#include <string>
#include <iostream>

using namespace std;

// DO not take in account only lower case letters can be
class Solution
{
public:
    int firstUniqChar(string s)
    {
        std::map<char, int> chars;

        for (const char c : s)
        {

            chars[c] += 1;
        }

        int non_repeated_index = -1;

        for (int i = 0; i <= s.size() - 1; i++)
        {
            if (chars.contains(s[i]) && chars[s[i]] == 1)
            {
                return i;
            }
        }

        return -1;
    }
};

int main()
{
    Solution s;
    std::cout << s.firstUniqChar("qweqrwteyrty") << std::endl;
    return 0;
}