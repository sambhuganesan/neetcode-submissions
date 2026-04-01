class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());

        for (int i = 1; i <= nums.length; i++) {
            subsetsA(nums, res, new ArrayList<>(), i, 0);
        }

        return res;
    }

    private void subsetsA(int[] nums, List<List<Integer>> res, List<Integer> sub, int size, int indx) {
        if (size == 0) {
            res.add(new ArrayList<>(sub));
            return;
        }

        for (int i = indx; i < nums.length; i++) {
            sub.add(nums[i]);
            subsetsA(nums, res, sub, size-1, i+1);
            sub.remove(sub.size() - 1);
        }
    }
}
