Relational Operators
A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:
<div>
== equal to</br>
!= not equal to</br>
> greater than</br>
< less than</br>
>= greater than or equal to</br>
<= less than or equal to</br>
</div>

Elif</br>
One or more elif statements (short for "else if") can be optionally added in between the if and else to provide additional condition(s) to check. Sometimes two is simply not enough.</br>

<code>if grade > 90:</br>
  print('A')</br>
elif grade > 80:</br>
  print('B')</br>
elif grade > 70:</br>
  print('C')</br>
elif grade > 60:</br>
  print('D')</br>
else:</br>
  print('F')</br>
</code>

Instructions
In chemistry, pH is a scale used to specify the acidity or basicity of a liquid.

Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

First, create a variable called ph and ask the user for a value between 0 and 14.

Write an if, elif, else statement that:

If ph is greater than 7, output "Basic".</br>
If ph is less than 7, output "Acidic".</br>
Else, output "Neutral".
