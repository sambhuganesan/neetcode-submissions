class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> subset;
        vector<vector<int>> res;
        subsets(0, nums, res, subset);

        return res;
    }

    void subsets(int i, vector<int>& nums, vector<vector<int>>& res, vector<int>& subset) {
        if (i == nums.size()){
            res.push_back(subset);
            return;
        }
        

        subset.push_back(nums[i]);
        subsets(i+1, nums, res, subset);

        subset.pop_back();
        subsets(i+1, nums, res, subset);
    }


};
