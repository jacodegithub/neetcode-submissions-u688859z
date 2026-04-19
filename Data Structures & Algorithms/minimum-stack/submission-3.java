class MinStack {
    private List<Integer> stack;
    private List<Integer> min_stack;

    public MinStack() {
        stack = new ArrayList<>();
        min_stack = new ArrayList<>();
    }
    
    public void push(int val) {
        stack.add(val);
        if (min_stack.isEmpty() || min_stack.get(min_stack.size() -1) >= val) {
            min_stack.add(val);
        }
    }
    
    public void pop() {
        if (stack.isEmpty()) {
            throw new RuntimeException("Stack is empty!");
        }
        if (stack.get(stack.size() - 1).equals(min_stack.get(min_stack.size() - 1))) {
            min_stack.remove(min_stack.size() - 1);
        }
        stack.remove(stack.size()-1);
    }
    
    public int top() {
        if (stack.isEmpty()) {
            throw new RuntimeException("Stack is empty!");
        }
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        if (min_stack.isEmpty()) {
            throw new RuntimeException("Stack is empty");
        }
        return min_stack.get(min_stack.size() - 1);
    }
}
