# Background

<a id="computers"></a>
## Computers

Computers are suited to solve problems that can be abstracted to be represented mathematically by *data*, such as measures, counts, facts, or labels, provided a method can be created to sove problems using that data.
*Programs* encode methods to solve problems.

Computers process data exceptionally faster and more accurately than humans.

Certain problems are especially appropriate to solve using computers.


<a id="python"></a>
## Python
Python is a programming language that simplifies writing programs.
Python allows organizing data to make writing programs easier and writing instructions to process that data.
It has several advantages over other programming languages.
- It is easier to learn than most programming languages.
- It is a widespread language, available on almost all types of computers.
- It has wide support for many common problems, and resources to learn how to solve them.
- It is easier to run and to develop programs than many languages.

<a id="mathematical-basics"></a>
## Mathematical basics
You must understand various mathematical concepts to program.
These sections include some programming specific information you may not have seen,
you might take a look even if you are familiar with them.
These include:

|Concept |Description |
|:- |:- |
|[Arithmetic](#arithmetic) |Basic operations and properties of numbers |
|[Algebra](#algebra) |Solves problems using mathematical expressions |
|[Number Systems](#number-systems)|Representing numbers as numerals |

### Arithmetic
Arithmetic includes basic operations and properties of numbers.

[Types of numbers](#Types-of-numbers)  
[Operations on numbers](#Operations-on-numbers)  
[Fractions](#Fractions)  
[Factoring](#Factoring)  
[Prime numbers](#Prime-numbers)  
[Factorials](#Factorials)  
[Exponents](#Exponents)  

<a id="number-types"></a><a id="Types-of-numbers"></a>
#### Types of numbers
The types of numbers are listed here.

|Number type |Description |Examples |
|:- |:- |:- |
|Natural numbers |All positive numbers starting with 1 | 1, 2, 3  |
|Whole numbers |All positive numbers starting with 0 |0, 1, 2, 3, 4 |
|Integers |All positive and negative numbers |-5, -4, -3, -2, -1, 0, 1, 2, 3, 4 |
|Decimals |Numbers with a decimal point and fraction |-4.1, 1.0, 3.1 |

<img src="https://raw.githubusercontent.com/kushnertodd/CFTM-intro-to-python/af686fa42bcc496cc70d56ba96b61afb75960a77/notebooks/Basic-math-number-line.png" width="827" height="142"/> 

This shows the relationships between the types.
- All natural numbers are whole numbers
- All whole numbers are integers
- All integers are decimals

<img src="https://raw.githubusercontent.com/kushnertodd/CFTM-intro-to-python/af686fa42bcc496cc70d56ba96b61afb75960a77/notebooks/Basic-math-number-types.png" width="341" height="341"/>

<a id="Operations-on-numbers"></a>
#### Operations on numbers
Kotlin allows the expected basic operations on numbers: Addition, Subtraction, Multiplication, Division, and Negation.
Kotlin also supports the Modulo operation which gives the remainder of a division, after one number is divided by another. 
These operations use slightly different symbols in a program, for example because multiplying using `x` can be confused with the letter x, and trying to multiply using ' $\cdot$ ' is impossible because that is not a keyboard symbol. 
For example, `8 % 3` is 2 as shown here.

<img src="https://raw.githubusercontent.com/kushnertodd/CFTM-intro-to-python/af686fa42bcc496cc70d56ba96b61afb75960a77/notebooks/Basic-math-modulo.png" width="200" height="200"/>

These operations have specific priorities for the order in which operations are applied. 
Negation has the highest priority, then multiplication, division, and modulo have the next priority, then addition and subtraction are the lowest.
Parentheses, `(` and `)`, are used to change the operation order. 


|Operation |Symbol |Program |Priority |
|:- |:- |:- |:- |
|Negation |`-` |`-` |highest |
|Multiplication |`x` or $\cdot$ |* |next highest | 
|Division |$\div$ |`/` |next highest | 
|Modulo |`%` |* |next highest | 
|Addition |`+` |`+` |lowest |
|Subtraction |`-` |`-` |lowest |

Operations of the same priority are applied left to right, so the order of operations for `3 + 6 - 2` is `(3 + 6) - 2`.
For operations of different priorities, in programs it might sometimes be clearer and less error prone to use parentheses even if they not necessary, so `5 + 8 / 4 - 2` might be written as `5 + (8 / 4) - 2`. 

<a id="Fractions"></a>
#### Fractions
Fractions are a way to show a number as divisions of another number.
The fraction $9 / 3$ shows the number of times 9 can be divided into groups of 3, which is 3.
Fractions may not represent a whole number, such as $7 / 2$, where 2 does not divide into 7 evenly.

There are a number of rules to combine fractions.

Rule |Example|
:- |:-
Addition|$\frac{a}{c}+\frac{b}{c}=\frac{a~+~b}{c}$|
Subtraction|$\frac{a}{c}-\frac{b}{c}=\frac{a-b}{c}$|
Multiplication|$\frac{a}{c}\cdot\frac{b}{c}=\frac{a\cdot b}{c}$|
Division|$\frac{a}{b}\div\frac{c}{d}=\frac{a}{b}\cdot\frac{d}{c}~$|

<a id="Factoring"></a>
#### Factoring
A number `N` may be a multiple of whole numbers `a`, `b`, `c`, etc.    

$N = a\cdot b\cdot c \cdot \cdots$  

The numbers `a`, `b`, `c`, etc. are the *factors* of `N`.
We say `N` is *evenly divisible* by  `a`, `b`, `c`, etc.

<a id="Prime-numbers"></a>
#### Prime numbers
A number always at least has two factors, 1 and itself.  

$N = 1 \cdot    N$  

A number that is only evenly divisible by 1 and itself is a *prime number*.

We say that when the factorization of `N` is

$N = a\cdot b\cdot c \cdot \cdots$   

if all of `a`, `b`, `c`, etc. are prime, that is the *prime factorization* of `N`.

<a id="Factorials"></a>
#### Factorials
A special case of factoring is when the factors of a number are all positive whole numbers less than or equal to `n`.
This number is the *factorial* of `n` or $n!$.

$n! = n \cdot (n - 1) \cdot (n - 2) \cdot\>\cdots\> \cdot 1$

<a id="Exponents"></a>
#### Exponents
Exponents are a way to represent repeated multiplication of the same number with fewer symbols. 
If a number is multiplied several times, the number of times it is multiplied can be represented with an *exponent*.
For example, multiplying 2 three times can be represented using an exponent of 3:

$\qquad 2 \cdot 2 \cdot 2 = 2^3 = 8 $

We say that $2^3$ is "two raised to the power 3".
The value 2 is the *base* of the exponent.
We can then do arithmetic on numbers with exponents.
We notice that is the same as 

$\qquad (2 \cdot 2) \cdot 2 = 2^2 \cdot 2^1 = 2^3$  

where $2^1$ is 2 "multiplied once".  

We notice a pattern that

$\qquad 2^2 \cdot 2^1 = 2^3 = 2^{2 + 1}$

so that when numbers with exponents are multiplied together, the exponents add.
There is one interesting result from this.
We can create a number with an exponent of 0, $2^0$, or "two multiplied 0 times", where it is not obvious what that means.
When we multiply that number by another number with an exponent we get

$\qquad 2^1 \cdot 2^0 = 2^{1 + 0} = 2$

What value is $2^0$? The only way to get that result is

$\qquad 2^1 \cdot 1 = 2$

Therefore $2^0$ must be 1.
That fact will be used in the [Hindu number system](./Number-systems.ipynb#Positional-number-systems).

##### Exponent rules
This is a list of all exponent rules.
Rule|Formula
|:- |:-
Product |$a^m \cdot a^n=a^{m + n}$  
Quotient |$a^m \div a^n=a^{m - n}$  
Power of a Power |$(a^m)^n=a^{mn}$  
Power of a Product |$(ab)^m=a^m\cdot b^m$  
Power of a Quotient |$(\frac{a}{b})^m=\frac{a^m}{b^m}$  
Zero Exponent |$a^0=1$  
Negative Exponent |$a^{-1}=\frac{1}{a^m}$  
Fractional Exponent |$a^{\frac{m}{n}}=\sqrt[n]{a^m}$  

##### Roots
The square *root* of a number `n` is the number which if multplied by itself will be `n`.  
$\qquad \sqrt{n} \cdot \sqrt{n} = (\sqrt{n})^2 = n$    
The cube root is the third root of `n`.   
$\qquad \sqrt[3]{n} \cdot \sqrt[3]{n} \cdot \sqrt[3]{n} = (\sqrt[3]{n})^3 = n$    

The fourth root is $\sqrt[4]{n}$, and so on.
We say this following the Fractional exponent rule.  
$\qquad \sqrt[n]{a}\>=\sqrt[n]{a^1}\>=\>a^{\frac{1}{n}}$ 

##### Logarithms

*Logarithms* are the reverse of exponents. 
If we say a number `N` has the value of a base `B` to the power `m`.
 
$N = B^m$

The logarithm of `N`, base `B`, is `m`. 

${log N}_B = m$

Logarithms are another convenient way to represent large numbers. For `N` = 1000000

$log_{10} N = log_{10} 1000000 = log_{10}\> 10^6 = 6$

### Algebra
Algebra finds unknown values using mathematical expressions.

[Variables](#Variables)  
[Substitution rule](#Substitution-rule)  
[Expressions](#Expressions)  
[Equations](#Equations)  

<a id="Variables"></a>
#### Variables
Variables are symbols for unknown values.
We can say the variable a has the value 1.

<a id="Substitution-rule"></a>
#### Substitution rule
Variables have the rule that they can be substituted by their value in any expresion.
If the value of a is 1, we can say the expression

a + 2

is the same as

1 + 2

<a id="Expressions"></a>
#### Expressions
Expressions are combinations of variables, values, and operators that give other values. 
An example of an expression is

a + (b $\cdot$ 4 - 1)

<a id="Equations"></a>
#### Equations
Equations say that two expressions separated by an equals sign = have the same value.
We can say that the variable a has the value 1 with the equation

a = 1

There are a number of rules for equations.

Rule |Example|Note
:- |:- |:-
Commutative|a+b=b+a|For addition
Commutative|a $\cdot$ b=b $\cdot$ a|For multiplication
Association|a+(b+c)=(a+b)+c|For addition
Association|a $\cdot$ (b $\cdot$ c)=(a $\cdot$ b) $\cdot$ c|For multiplication
Identity|a + 0 = a|for addition
Identity|a - 0 = a|for subtraction
Identity|a - a = 0|for subtraction
Identity|-a + a = 0|for subtraction
Identity|a $\cdot$ 1 = a|for multiplication
Identity|a $\div$ 1 = a|for division
Identity|a $\div$ a = 1|for division

Note that the Commutative and Association rules do not apply for substraction and division.

These are rules for changing equations.

Rule| If |Then
:- |:- |:-
Adding constants|a = b|a + c = b + c|
Subtracting constants|a = b|a - c = b - c|
Multiplying by constants|a = b|a $\cdot$ c=b $\cdot$ c|
Dividing by constants|a = b|a $\div$ c=b $\div$ c|
Inverse of adding|a = b + c|a - c = b|
Inverse of subtracting|a = b - c|a + c = b|
Inverse of multiplying|a = b $\cdot$ c|a $\div$ c = b|
Inverse of dividing|a = b $\div$ c|a $\cdot$ c = b|

We can use these rules to find the value of a variable in an equation.
In the equation

a - 2 = 1

We can change the equation to solve for a.

Equation|Rule
:- |:-
a - 2 + 2 = 1 + 2|Adding constant 2  
a - 0 = 3|Identity for subtraction (-2 + 2 = 0)
a = 3|Identity for subtraction

We can solve for equations with two variables.
If we have

b - 1 = 2  
a + b - 1 = 6  

We can use these rules to solve for a and b.

Equation|Rule
:- |:-
a + 2 = 6|Substitution (2 for b - 1)  
a = 6 - 2|Inverse of adding
a = 4|

Then we have

Equation|Rule
:- |:-
4 + b - 1 = 6|Substitution
b + 3 = 6|Subtraction
b + 3 - 3 = 6 - 3|Subtracting constant 3
b + 0 = 3|Identity for subtraction
b = 3|Identity for addition
