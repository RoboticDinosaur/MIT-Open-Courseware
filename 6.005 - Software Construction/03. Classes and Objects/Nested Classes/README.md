# Questions and Exercises: Nested Classes

## Questions

1. The program Problem.java doesn't compile. What do you need to do to make it compile? Why?
   ```
   public class Problem {
       String s;
       static class Inner {
           void testMethod() {
               s = "Set from Inner";
           }
       }
   }
   ```
   **Answer:** Change *class Inner* from static.

2. Use the Java API documentation for the *Box* class (in the *javax.swing* package) to help you answer the following questions.

    1. What static nested class does *Box* define?
        **Answer:** Box.Filler

    2. What inner class does *Box* define?
        **Answer:** Box.AccessibleBox

    3. What is the superclass of *Box*'s inner class?
        **Answer:** java.awt.Container.AccessibleAWTContainer

    4. Which of *Box*'s nested classes can you use from any class?
        **Answer:** Box.Filler

    5. How do you create an instance of *Box*'s *Filler* class?
        **Answer:** new Box.Filler(min, pref, max)

## Exercises

1. Get the file Class1.java. Compile and run Class1. What is the output?
   **Answer:**
   InnerClass1: getString invoked.
   InnerClass1: getAnotherString invoked.

2. The following exercises involve modifying the class DataStructure.java, which the section Inner Class Example discusses.

    1. Define a method named print(DataStructureIterator iterator). Invoke this method with an instance of the class EvenIterator so that it performs the same function as the method printEven.

    2. Invoke the method print(DataStructureIterator iterator) so that it prints elements that have an odd index value. Use an anonymous class as the method's argument instead of an instance of the interface DataStructureIterator.

    3. Define a method named print(java.util.Function<Integer, Boolean> iterator) that performs the same function as print(DataStructureIterator iterator). Invoke this method     with a lambda expression to print elements that have an even index value. Invoke this method again with a lambda expression to print elements that have an odd index value.

    4. Define two methods so that the following two statements print elements that have an even index value and elements that have an odd index value:

        ```
        DataStructure ds = new DataStructure()
        // ...
        ds.print(DataStructure::isEvenIndex);
        ds.print(DataStructure::isOddIndex);
        ```