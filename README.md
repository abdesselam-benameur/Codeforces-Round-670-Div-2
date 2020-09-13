# Subset Mex

My solution to [Problem A](https://codeforces.com/contest/1406/problem/A) in [Codeforces Round #670 (Div. 2)](https://codeforces.com/contest/1406)

Here it is the problem statement:

> Given a set of integers (it can contain equal elements).
>
> You have to split it into two subsets $A$ and $B$ (both of them can contain equal elements or be empty). You have to maximize the value of  $mex(A)+mex(B)$.
>
> Here $mex$ of a set denotes the smallest non-negative integer that doesn't exist in the set. For example:
>
> - $mex(\{1,4,0,2,2,1\})=3$
> - $mex(\{3,3,2,1,3,0,0\})=4$
> - $mex(∅)=0 \text{ (mex for empty set)}$
>
> The set is split into two subsets $A$ and $B$ if for any integer number $x$ the number of occurrences of $x$ into this set is equal to the sum of the number of occurrences of $x$ into $A$ and the number of occurrences of $x$ into $B$.
>
> #### Input
>
> The input consists of multiple test cases. The first line contains an integer $t$  $(1\leq t\leq 100)$ — the number of test cases. The description of the test cases follows.
>
> The first line of each test case contains an integer $n$ $(1\leq n\leq 100)$— the size of the set.
>
> The second line of each testcase contains $n$ integers $a_1,a_2,\dots a_n$ $(0\leq a_i\leq 100)$ — the numbers in the set.
>
> #### Output
>
> For each test case, print the maximum value of $mex(A)+mex(B)$.
>
> #### Example
>
> input
>
> ```
> 4
> 6
> 0 2 1 5 0 1
> 3
> 0 1 2
> 4
> 0 2 0 1
> 6
> 1 2 3 4 5 6
> ```
>
> output
>
> ```
> 5
> 3
> 4
> 0
> ```
>
> **Note**
>
> In the first test case, $A=\left\{0,1,2\right\},B=\left\{0,1,5\right\}$ is a possible choice.
>
> In the second test case, $A=\left\{0,1,2\right\},B=\varnothing$ is a possible choice.
>
> In the third test case, $A=\left\{0,1,2\right\},B=\left\{0\right\}$ is a possible choice.
>
> In the fourth test case, $A=\left\{1,3,5\right\},B=\left\{2,4,6\right\}$ is a possible choice.