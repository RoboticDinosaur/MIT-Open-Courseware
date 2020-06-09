# Questions and Exercises: Characters and Strings

## Questions

1. What is the initial capacity of the following string builder?
    ```
    StringBuilder sb = new StringBuilder("Able was I ere I saw Elba.");
    ```
    **Answer:** 16

2. Consider the following string:
    ```
    String hannah = "Did Hannah see bees? Hannah did.";
    ```

    2. What is the value displayed by the expression hannah.length()?
        **Answer:** 32

    3. What is the value returned by the method call hannah.charAt(12)?
        **Answer:** e

    4. Write an expression that refers to the letter b in the string referred to by hannah.
        **Answer:** hanna.charAt(15)

3. How long is the string returned by the following expression? What is the string?
    ```
    "Was it a car or a cat I saw?".substring(9, 12)
    ```
    **Answer:** car

4. In the following program, called ComputeResult, what is the value of result after each numbered line executes?
    ```
    public class ComputeResult {
        public static void main(String[] args) {
            String original = "software";
            StringBuilder result = new StringBuilder("hi");
            int index = original.indexOf('a');
    /*1*/   result.setCharAt(0, original.charAt(0)); "si"
    /*2*/   result.setCharAt(1, original.charAt(original.length()-1)); "se"
    /*3*/   result.insert(1, original.charAt(4)); "sew"
    /*4*/   result.append(original.substring(1,4)); "sewoftw"
    /*5*/   result.insert(3, (original.substring(index, index+2) + " ")); "sewoar ftw"

            System.out.println(result);
        }
    }
    ```

## Exercises

1. Show two ways to concatenate the following two strings together to get the string "Hi, mom.":
    ```
    String hi = "Hi, ";
    String mom = "mom.";
    ```

2. Write a program that computes your initials from your full name and displays them.

3. An anagram is a word or a phrase made by transposing the letters of another word or phrase; for example, "parliament" is an anagram of "partial men," and "software" is an anagram of "swear oft." Write a program that figures out whether one string is an anagram of another string. The program should ignore white space and punctuation.
