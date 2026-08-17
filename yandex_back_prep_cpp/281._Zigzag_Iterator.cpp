#include <vector>
#include <deque>
#include <iostream>

using namespace std;

class ZigzagIterator
{
public:
    ZigzagIterator(vector<int> &v1, vector<int> &v2)
    {
        if (v2.size() > 0)
        {
            this->queue.push_back(std::deque<int>(v2.begin(), v2.end()));
        }

        if (v1.size() > 0)
        {
            this->queue.push_back(std::deque<int>(v1.begin(), v1.end()));
        }
    }

    int next()
    {

        deque<int> v = this->queue.back();
        queue.pop_back();

        int val = v.front();
        v.pop_front();

        if (v.size() > 0)
        {
            this->queue.push_front(v);
        }

        return val;
    }

    bool hasNext()
    {
        return this->queue.size() > 0;
    }

private:
    std::deque<std::deque<int>> queue;
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */

int main()
{

    std::vector<int> v1 = {1, 2, 3};
    std::vector<int> v2 = {4, 5, 6};

    ZigzagIterator *zi = new ZigzagIterator(v1, v2);

    while (zi->hasNext())
    {
        std::cout << zi->next() << std::endl;
    }

    return 0;
}