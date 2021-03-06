# Questions

1. What's wrong with the following program?
    ```
    public class SomethingIsWrong {
        public static void main(String[] args) {
            Rectangle myRect;
            myRect.width = 40;
            myRect.height = 50;
            System.out.println("myRect's area is " + myRect.area());
        }
    }    
    ```
    **Answer:** There is no "new" object created.

2. The following code creates one array and one string object. How many references to those objects exist after the code executes? Is either object eligible for garbage collection?

    ```
    ...
    String[] students = new String[10];
    String studentName = "Peter Parker";
    students[0] = studentName;
    studentName = null;
    ...    
    ```
    **Answer:** One reference for each so neither is eligible for garbage collection.

3. How does a program destroy an object that it creates? 
    **Answer:** When it has no more references it is garbage collected.
    __RIGHT__ It doesn't, it can only make an object eligible for garbage collection.

# ExercisesExercises

1. Fix the program called SomethingIsWrong shown in Question 1.
    
2. Given the following class, called NumberHolder, write some code that creates an instance of the class, initializes its two member variables, and then displays the value of each member variable.
    ```
    public class NumberHolder {
        public int anInt;
        public float aFloat;
    }
    ```