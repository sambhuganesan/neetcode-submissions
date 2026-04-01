class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        res.add(new ArrayList<>());

        for (int i = 1; i <= nums.length; i++) {
            subsets(nums, res, new ArrayList<>(), i, 0);
        }

        return res;
    }

    private void subsets(int[] nums, List<List<Integer>> res, List<Integer> sub, int size, int indx) {
        if (size == 0) {
            res.add(new ArrayList<>(sub));
            return;
        }

        for (int i = indx; i < nums.length; i++) {
            if (i > indx && nums[i] == nums[i-1]) continue;
            sub.add(nums[i]);
            subsets(nums, res, sub, size-1, i+1);
            sub.remove(sub.size() - 1);
        }
    }
}
