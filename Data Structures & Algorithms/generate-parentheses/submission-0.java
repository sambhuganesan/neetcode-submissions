class Solution {
    public List<String> generateParenthesis(int n) {
        List<List<Character>> result = new ArrayList<>();
        List<Character> s = new ArrayList<>();
        int num_of_L = n;
        int num_of_R = n;

        genParam(num_of_L, num_of_R, s, result);

        List<String> output = new ArrayList<>();
        for (int i = 0; i < result.size(); i++) {
            String str = "";
            for (int j = 0; j < result.get(i).size(); j++) {
                str += result.get(i).get(j);
            }
            output.add(str);
        }

        return output;
    }

    private void genParam(int num_of_L, int num_of_R, List<Character> s, List<List<Character>> result) {
        if (num_of_L == 0 && num_of_R == 0) {
            result.add(new ArrayList<>(s));
            return;
        }

        if (num_of_L > 0) {
            s.add('(');
            genParam(num_of_L - 1, num_of_R, s, result);
            s.remove(s.size() - 1);
        }
        
        if (num_of_L < num_of_R) {        
            s.add(')');
            genParam(num_of_L, num_of_R - 1, s, result);
            s.remove(s.size() - 1);
        }
    }
}
