
import exceptions.*;
import java.util.Iterator;

/**
 * Represents a linked implementation of a stack.
 *
 * @author Java Foundations 
 * @version 4.0
 */
public class DropOutStack<T> implements StackADT<T>
{
    private int count;  
    private LinearNode<T> top; 
    private final int DEFAULT = 3;
    private int limit = DEFAULT;
	private LinearNode<T> temp;
	private LinearNode<T> previous;

    /**
     * Creates an empty stack.
     */
    public DropOutStack(Integer n)
    {
        count = 0;
        top = null;
        if (limit <= 0)
        		limit = DEFAULT;
        else
        	limit = n;
    }

    /**
     * Adds the specified element to the top of this stack.
     * @param element element to be pushed on stack
     */
    public void push(T element)
    {
        LinearNode<T> temp = new LinearNode<T>(element);
        temp.setNext(top);
        top = temp;
        count++;
        if(count > limit)
        {
        	dropBottom();
        	count --;
        }
        
    }
    
    /*
     * removes the element at the bottom of the stack,
     * this method should be called whenever the stack reaches its capacity.
     */
    public void dropBottom()
    {
    	temp = top;
    	previous = top;
    	while(temp.getNext()!=null) {
    		previous = temp;
    		temp = temp.getNext();
    	}
    	previous.setNext(null);
    	
    }

  

	/**
     * Removes the element at the top of this stack and returns a
     * reference to it. 
     * @return element from top of stack
     * @throws EmptyCollectionException if the stack is empty
     */
    public T pop() throws EmptyCollectionException
    {
        if (isEmpty())
            throw new EmptyCollectionException("stack");

        T result = top.getElement();
        top = top.getNext();
        count--;
 
        return result;
    }
   
    /**
     * Returns a reference to the element at the top of this stack.
     * The element is not removed from the stack.  
     * @return element on top of stack
     * @throws EmptyCollectionException if the stack is empty  
     */
    public T peek() throws EmptyCollectionException
    {
    	if(isEmpty())
    		throw new EmptyCollectionException("stack");
        T result = top.getElement();
        return result;
        }

    /**
     * Returns true if this stack is empty and false otherwise. 
     * @return true if stack is empty
     */
    public boolean isEmpty()
    {
        // To be completed as a Programming Project
    	return (count == 0);
    }
 
    /**
     * Returns the number of elements in this stack.
     * @return number of elements in the stack
     */
    public int size()
    {
        // To be completed as a Programming Project
    	return count;
    }

    /**
     * Returns a string representation of this stack. 
     * @return string representation of the stack
     */
    public String toString()
    {
        // To be completed as a Programming Project
    	String result = "";
    	LinearNode current = top;
    	while (current != null)
    	{
    		result=result+current.getElement()+"\n";
    		current=current.getNext();
    	}
    	return result;
    }
    public static void main(String args[]){
    	DropOutStack testStack = new DropOutStack(4);
    	System.out.println("testing a drop-out stack with capacity " + testStack.limit);
    	
		testStack.push("1");
		testStack.push("2");
		testStack.push("3");
		System.out.println("After pushing 3 elements, the stack is \n" + testStack);
		testStack.push("4");
		System.out.println("After pushing the 4th elements, the stack is \n");
		System.out.println(testStack);
	    System.out.println("after popping the top element, the stack is");
	    testStack.pop();
	    System.out.println(testStack);
	    testStack.push("5");
		System.out.println("After pushing the 5th elements, the stack is \n" + testStack);
		testStack.push("6");
		System.out.println("After pushing the 6th elements, the stack is \n" + testStack);

	    
	    System.out.println("current size of the stack is "+ testStack.size());
	    System.out.println("peek operation returns: " + testStack.peek());
	  

    }
}
