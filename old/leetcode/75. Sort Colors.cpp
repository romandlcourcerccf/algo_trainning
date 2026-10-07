class Solution {
public:
    void sortColors(vector<int>& nums) {
        int h[3];
        for (int i = 0; i<3; i++) {
            h[i] = 0;
        }

        for (int i = 0; i < nums.size(); i++) {
            h[nums[i]] +=1;
        }

        int pos = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = pos; j < pos + h[i]; j++) {
                pos +=1;
                nums.at(j) = i;
            }
        }

        return;

    }
};