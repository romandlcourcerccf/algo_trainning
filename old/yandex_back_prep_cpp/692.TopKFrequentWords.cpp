#include <iostream>
#include <queue>
#include <vector>
#include <map>

using namespace std;

struct Pair
{
    int frequency;
    std::string str;
};

struct Comparator
{
    bool operator()(const Pair &p1, const Pair &p2)
    {
        return p1.frequency < p2.frequency;
    }
};

class Solution
{
public:
    vector<string> topKFrequent(vector<string> &words, int k)
    {
        std::priority_queue<Pair, std::vector<Pair>, Comparator> max_heap;
        std::map<std::string, int> words_counter;

        for (std::string word : words)
        {
            words_counter[word] += 1;
        }

        for (const auto &[key, value] : words_counter)
        {

            Pair pair{
                .str = key,
                .frequency = value

            };

            max_heap.push(pair);
        }

        std::vector<std::string> result;

        while (k > 0)
        {
            Pair pair = max_heap.top();
            result.push_back(pair.str);
            max_heap.pop();
            k--;
        }

        return result;
    }
};

int main()
{

    std::vector<std::string> words = {"i", "love", "leetcode", "i", "love", "coding"};
    int k = 2;

    Solution s;
    std::vector<string> res = s.topKFrequent(words, k);

    for (std::string const &s : res)
    {
        std::cout << s << " ";
    }
    std::cout << std::endl;
}
