class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> subset;
        vector<vector<int>> res;

        combinations(0, nums, subset, res, target);
        return res;

    }

    void combinations(int i, vector<int>& nums, vector<int>& subset, vector<vector<int>>& res, int target) {
        if (target < 0 || i >= nums.size()) {
            return;
        }

        if (target == 0) {
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[i]);
        combinations(i, nums, subset, res, target - nums[i]);
        subset.pop_back();
        combinations(i+1, nums, subset, res, target);

    }
};
