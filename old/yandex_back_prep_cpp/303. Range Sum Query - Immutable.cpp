class NumArray
{
public:
    NumArray(vector<int> &nums)
    {
        this->prefix = std::vector<int>(nums.size() + 1, 0);

        for (int i = 1; i < prefix.size(); i++)
        {
            prefix[i] = prefix[i - 1] + nums[i - 1];
        }
    }

    int sumRange(int left, int right)
    {
        return this->prefix[right + 1] - this->prefix[left];
    }

    std::vector<int> prefix;
};