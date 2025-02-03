# Overview

This repository contains a method `bisection()` for running a bisection method on a function in `src.bisection.py` to determine a zero along an interval $x \in [a, b]$. Also included is a series of tests to confirm its functionality.

# Algorithm

1. Starting with a function $f(x)$ with two guesses $A = f(a)$ and $B=f(b)$ where $\text{sign}(a) \neq \text{sign}(b)$.
2. Determine the current interval's midpoint $m = \frac{a+b}{2}$ and its function value $M=f(m)$.
3. If $M = 0$, return $m$. If $\text{sign}(m) = a$, repeat the method along the interval $x \in [m, b]$. Otherwise, repeat the method along the inverval $x \in [a, m]$.
4. Repeat this until either the tolerance is reached ($|M| \leq \text{tol}$) or until the stated maximum iterations is reached.

# Installation

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name bisection-method-env python=3.9.18
```
Once the environment has been created, activate it:

```bash
conda activate bisection-method-env
```
Double check that python is version 3.9.18 in the environment. It should still work on a later version, but it was made on this one.
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
Test that the code is working with pytest:
```bash
pytest -v --cov=bisectionmethod --cov-report term-missing
```
Code coverage should be 100%. Now you are prepared to write your own code based on this method and/or run the tutorial.