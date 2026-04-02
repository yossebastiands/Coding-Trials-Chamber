// Java Program to demonstrate
// Variables

class JavaVariables {
    // instance variable
    public int revise;

    // static variable
    public static int count = 0;

    public static void help(int i)
    {
        // here int i is local variable
        // changes will not affect original value
        JavaVariables.count++;
        System.out.println(i);
    }

    public static void main(String[] args)
    {
        // local variable
        int i = 10;

        System.out.println("Before Calling function count:"
                           + JavaVariables.count);
      
        help(i);
        System.out.println("After Calling function count:"
                           + JavaVariables.count);

        JavaVariables temp = new JavaVariables();
        temp.revise = i + count;

        System.out.println("Instance variable value:"
                           + temp.revise);
    }
}