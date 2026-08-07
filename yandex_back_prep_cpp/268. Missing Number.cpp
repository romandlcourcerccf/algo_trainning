class Solution
{
public:
    int missingNumber(vector<int> &nums)
    {
        std::map<int, int> counter;
        int num_size = nums.size() + 1;

        for (int n : nums)
        {
            if (!counter.contains(n))
            {
                counter[n] = 1;
            }
            else
            {
                counter[n] = counter[n] + 1;
            }
        }

        for (int i = 0; i < num_size; i++)
        {
            if (!counter.contains(i))
            {
                return i;
            }
        }

        return 0;
    }
};