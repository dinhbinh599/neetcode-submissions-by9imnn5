public class MinStack {

    public Stack<int> obj;
    public Stack<int> min;

    public MinStack() {
        obj = new Stack<int>();
        min = new Stack<int>();
    }
    
    public void Push(int val) {
        obj.Push(val);
        if (min.Count != 0){
            min.Push(Math.Min(val, min.Peek()));
        }
        else {
            min.Push(val);
        }
    }
    
    public void Pop() {
        obj.Pop();
        min.Pop();
    }
    
    public int Top() {
        return obj.Peek();
    }
    
    public int GetMin() {
        return min.Peek();
    }
}
