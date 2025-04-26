# Linear Equation Solver

With all its built-in features, NumPy turns Python into a complex, but very powerful calculating tool.

## Problem Description

Write a function `solveEqns(eqn1, eqn2)` that takes a system of linear equations in the form of 2 string parameters. Both of the parameters have the form "a x + b y = c", with a, b and c being integer numbers.

The function should solve this system of linear equations for x and y using the built-in solver of NumPy, and return the result as a 2-element tuple.

## Example

For example, if `eqn1` is "1 x + 0 y = 1", and `eqn2` is "1 x + 1 y = 3", the function should return (1.0, 2.0).

## Hint

You can assume that a, b and c are never negative, and that there always exists one correct solution.
Hint: You can make use of the fact that the equation strings always follow a very structured pattern, so that it should be easy to extract the relevant numbers without any complicated logic or loops.

Your code snippet should define the following variables:

- `soleEqns` (funtion) solves a system of 2 linear equations
