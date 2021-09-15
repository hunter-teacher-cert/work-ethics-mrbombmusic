These programs demonstrate the python skills I have acquired over the past two weeks.

**cgol.py** is a recreation of the Conway's Game of Life project we did in Java.
It includes using 2D lists in python.


The following programs were used to solve problems found on the **Project Euler** website.
The project directions are provided as well as a link to the problem on the website.

### password.py

includes:
- Reading and parsing .txt file
- lists
- dictionaries
- functions

[Project Euler Link](https://projecteuler.net/problem=79)


A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, passkey.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

### amicable.py

includes:
- lists
- recursion
- functions

[Project Euler Link](https://projecteuler.net/problem=95)

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

### anagrams.py

includes:
- Reading and parsing .txt file
- lists
- dictionaries
- functions

[Project Euler Link](https://projecteuler.net/problem=98)

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt, a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs.

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
