#include <map>
#include <queue>

using namespace std;

struct FreqStruct{
    int val;
    int key;
    
    bool operator < (const FreqStruct& other) const {
        return key < other.key;
    }
};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        vector<int> result;

        map <int, int> freq_counter;
        priority_queue<FreqStruct> minHeap;

        for (int n : nums) {
            freq_counter[n] +=1;
        }

        for (auto const& x: freq_counter) {
            minHeap.push({x.first, x.second});
        }

        int _k = 0;
        while (_k < k){
            result.push_back(minHeap.top().val);
            minHeap.pop();
            _k++;
        }

        return result;

    }
};