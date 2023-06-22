Random</br>
In Python, modules are .py files containing Python code that can be imported inside another Python program. The Python standard library contains well over 200 modules that we can use.</br>

We can use the .randint() function from a module called random to generate a random number from a range.</br>

But first, let's import this module so we can use its functions.</br>

<code>import random</code>

Next, we'll create a variable to store the randomly generated value. Declare a variable called num, and assign it to the function call:</br>

<code>num = random.randint(1, 9)</code>

This will generate a random number between 1 and 9 (inclusive of both).</br>

Together, the code will look like:</br>

<code>import random</code>

<code>num = random.randint(1, 9)</code>

<code>print(num)</code>

The output should be different each time it runs: 2, 8, 5, 9, 2, 1, 3...</br>

# Instructions</br>
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940's for fortune-telling and advice seeking. 🎱</br>

It's an oversized 8 ball with some of the following answers:</br>

Yes - definitely.</br>
It is decidedly so.</br>
Without a doubt.</br>
Reply hazy, try again.</br>
Ask again later.</br>
Better not tell you now.</br>
My sources say no.</br>
Outlook not so good.</br>
Very doubtful.</br>
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.</br>

The output should have the following format:</br>

Question:      [Question]</br>
Magic 8 Ball:  [Answer]

For example:</br>

Question:      Is Codédex better than Udemy yet?</br>
Magic 8 Ball:  Better not tell you now.
