class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        permutations(nums, res, new ArrayList<>(), new boolean[nums.length]);
        return res;
    }

    private void permutations(int[] nums, List<List<Integer>> res, List<Integer> perm, boolean[] used) {        
        if (perm.size() == nums.length) {
            res.add(new ArrayList<>(perm));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            perm.add(nums[i]);
            permutations(nums, res, perm, used);
            perm.remove(perm.size() - 1);
            used[i] = false;
        }
    }
}
