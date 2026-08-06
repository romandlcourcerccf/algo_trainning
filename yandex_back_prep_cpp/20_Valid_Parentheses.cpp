#include <set>
#include <iostream>

using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        std::vector<char> stack;

        for (const char c : s)
        {

            if (c == '(' | c == '{' | c == '[')
            {
                stack.push_back(c);
            }
            else
            {
                if (stack.size() == 0)
                {
                    return false;
                }

                char left = stack.back();
                stack.pop_back();

                std::string _s({left, c});
                if (!(_s == "{}" || _s == "[]" || _s == "()"))
                {
                    return false;
                }
            }
        }

        if (stack.size() == 0)
        {
            return true;
        }

        return false;
    }
};

int main()
{

    Solution s;
    bool res = s.isValid(std::string("(){}}"));

    std::cout << "res :" << res << std::endl;

    return 0;
}