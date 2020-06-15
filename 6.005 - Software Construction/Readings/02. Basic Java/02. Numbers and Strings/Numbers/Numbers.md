# Numbers

## Questions

1. Use the API documentation to find the answers to the following questions:
   1. What _Integer_ method can you use to convert an _int_ in to a string that expresses the number in hexadecimal? For example, what method converts the integer 65 in to the string "41"?
      **Answer:** toHexString(int i)

   2. What _Integer_ method would you use to convert a string expressed in base 5 into the equivalent _int_? for example, how would you convert the string "230" into the integer value 65? Show the code you would use to accomplish this task.
      **Answer:**  toString(int i, int radix)

   3. What Double method can you use to detect whether a floating-point number has the special vvalue Not a Number (_Nan_)?
      **Answer:** isNaN(double v)

2. What is the value of the following expression, and why?
   `Integer.valueOf(1).equals(Long.valueOf(1))`
   **Answer:** True because 1 is the same value as a Long and an Integer

## Exercises

1. Change MaxVariablesDemo to show minimum values instead of maximum values. You can delete all code related to the variables aChar and aBoolean. What is the output?
   
   ```
   The largest byte value is -128.
   The largest short value is -32768.
   The largest integer value is -2147483648.
   The largest long value is -9223372036854775808.
   The largest float value is 1.4E-45.
   The largest double value is 4.9E-324.
   ```

2. Create a program that reads an unspecified number of integer arguments from the command line and adds them together. For example, suppose that you enter the following:
   
   `java Adder 1 3 2 10`

   The program should display 16 and then exit. The program should display an error message if the user enters only one argument. You can base your program on ValueOfDemo.
3. Create a program that is similar to the previous one but has the following differences:

    * Instead of reading integer arguments, it reads floating-point arguments.
    * It displays the sum of the arguments, using exactly two digits to the right of the decimal point.

   For example, suppose that you enter the following:

   `java FPAdder 1 1e2 3.0 4.754`

   The program would display 108.75. Depending on your locale, the decimal point might be a comma (,) instead of a period (.).

