class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r)
        {
            int middle = (l + r) / 2;
            if (nums[middle] == target)
            {
                return middle;
            }
            else if (nums[middle] < target)
            {
                l = middle + 1;
            }
            else
            {
                r = middle - 1;
            }
        }

        return -1;
    }
};