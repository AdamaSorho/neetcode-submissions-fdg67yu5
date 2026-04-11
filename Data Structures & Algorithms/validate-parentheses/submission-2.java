class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        Stack<Character> stack = new Stack<>();

        for (char c: s.toCharArray()) {
            if (map.containsKey(c)) {
                stack.push(c);
            }
            else if (stack.empty() || map.get(stack.pop()) != c) {
                return false;
            }
        }

        return stack.empty();
    }
}
