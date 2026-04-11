class Solution {
    public int evalRPN(String[] tokens) {
        Map<String, Integer> operators = new HashMap<>();
        operators.put("+", 1);
        operators.put("-", 2);
        operators.put("*", 3);
        operators.put("/", 4);

        Stack<Integer> stack = new Stack<>();

        for (String s: tokens) {
            if (operators.containsKey(s)) {
                int b = stack.pop();
                int a = stack.pop();
                int result;
                if (operators.get(s) == 1) {
                    result = a + b;
                }
                else if (operators.get(s) == 2) {
                    result = a - b;
                }
                else if (operators.get(s) == 3) {
                    result = a * b;
                }
                else {
                    result = a / b;
                }
                stack.push(result);
            }
            else {
                stack.push(Integer.valueOf(s));
            }
        }

        return stack.pop();
    }
}
