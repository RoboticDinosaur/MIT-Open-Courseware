# Questions and Exercises: Getting Started

## Questions

1. When you compile a program written in the Java programming language, the compiler converts the human-readable source file into platform-independent code that a Java Virtual Machine can understand. What is this platform-independent code called?

2. Which of the following is not a valid comment:
    1. /** comment */
    2. /* comment */
    3. /* comment
    4. // comment
    **Answer:** 3 is an incorrect comment without its closing tag.

3. What is the first thing you should check if you see the following error at runtime:
    ```
    Exception in thread "main" java.lang.NoClassDefFoundError:
    HelloWorldApp.java.
    ```
    **Answer:** That your class is named correctly.

4. What is the correct signature of the main method?
   **Answer:** public static void main(Type Argument) {}

5. When declaring the main method, which modifier must come first, public or static?
   **Answer:** public

6. What parameters does the main method define?
    **Answer:** application arguments.    

## Exercises

1. Change the HelloWorldApp.java program so that it displays Hola Mundo! instead of Hello World!.

2. You can find a slightly modified version of HelloWorldApp here: *HelloWorldApp2.java*
    
    The program has an error. Fix the error so that the program successfully compiles and runs. What was the error?
    **Answer:** It didn't have a closing quotation on "Hello world!"