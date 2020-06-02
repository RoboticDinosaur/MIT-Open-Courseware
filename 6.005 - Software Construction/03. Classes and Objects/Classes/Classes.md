# Questions

    1. Consider the following class:

        public class IdentifyMyParts {
            public static int x = 7; 
            public int y = 3; 
        }

        1. What are the class variables? int x

        2. What are the instance variables? int y

        3. What is the output from the following code:

            IdentifyMyParts a = new IdentifyMyParts();
            IdentifyMyParts b = new IdentifyMyParts();
            a.y = 5;
            b.y = 6;
            a.x = 1;
            b.x = 2;
            System.out.println("a.y = " + a.y); // 5
            System.out.println("b.y = " + b.y); // 6
            System.out.println("a.x = " + a.x); // 2
            System.out.println("b.x = " + b.x); // 2
            System.out.println("IdentifyMyParts.x = " + IdentifyMyParts.x); // 2

# Exercises

1. Write a class whose instances represent a single playing card from a deck of cards. Playing cards have two distinguishing properties: rank and suit. Be sure to keep your solution as you will be asked to rewrite it in Enum Types.
    ```
    Hint: 

    You can use the assert statement to check your assignments. You write:

    assert (boolean expression to test); 

    If the boolean expression is false, you will get an error message. For example,

    assert toString(ACE) == "Ace";

    should return true, so there will be no error message.

    If you use the assert statement, you must run your program with the ea flag:

    java -ea YourProgram.class
    ```

    2. Write a class whose instances represent a full deck of cards. You should also keep this solution.

    3. Write a small program to test your deck and card classes. The program can be as simple as creating a deck of cards and displaying its cards.
