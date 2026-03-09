# Homework 8

### Linear Regression

This homework covers several regression topics and will give you practice with the numpy and sklearn libraries in Python. It has both a coding and a writeup component.

## Goals

In this homework you will:

1. Build linear regression models to serve as predictors from input data.
2. Parse input data into feature matrices and target variables.
3. Use cross validation to find the best regularization parameter for a dataset.

## Background

Before attempting the homework, please review the notes on linear regression. In addition to what is covered there, the following background may be useful.

### CSV Processing in Python

Like `.txt`, `.csv` (comma-separated values) is a useful file format for storing data. In a CSV file, each line is a data record, and different fields of the record are separated by commas, forming a two-dimensional data table (records by fields). Typically, the first row and first column are headings for the fields and records.

Python’s **pandas** module helps manage two-dimensional data tables.

We can read a CSV as follows:

```python
import pandas as pd

data = pd.read_csv('data.csv')
```

To see a small snippet of the data, including the headers:

```python
data.head()
```

If we want to use columns `'A'`, `'B'`, `'D'` as features and `'C'` as the target variable:

```python
X = data[['A', 'B', 'D']]
y = data[['C']]
```

More details on Pandas can be found here:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

### Matrix Algebra in Python

Python offers computationally efficient functions for linear algebra operations through the **numpy** library.

Suppose `A` is a list of `m` lists, each having `n` numerical items. Numpy will treat `A` as an `m × n` matrix.

To transpose `A`:

```python
import numpy as np

AT = A.T
```

If `B` is another `m × n` matrix, we can compute:

```python
AB = A.T @ B
```

If `n = 1`, meaning `A` and `B` are vectors, this operation becomes the **dot product**.

If `A` is a square `n × n` matrix, we can compute its inverse:

```python
Ainv = np.linalg.inv(A)
```

More matrix operations:

https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

### Linear Regression in Python

Python offers several machine learning models through the **sklearn** library.

Example linear regression model:

```python
from sklearn.linear_model import LinearRegression

model_lin = LinearRegression(fit_intercept=True)
model_lin.fit(X, y)
```

Predicting new values:

```python
yn = model_lin.predict(Xn)
```

Viewing model parameters:

```python
model_lin.get_params()
```

Ridge regression example:

```python
from sklearn.linear_model import Ridge

model_ridge = Ridge(alpha=0.2, fit_intercept=True)
model_ridge.fit(X, y)
```

More regression models:

https://scikit-learn.org/stable/supervised_learning.html#supervised-learning

## Instructions

### Setting up your repository

Click the link on Piazza to set up your repository for Homework 8, then clone it.

Your repository should contain the following files:

1. `polyfit.py`, a starter file for Problem 1
2. `poly.txt`, a data file for Problem 1
3. `regularize-cv.py`, a starter file for Problem 2
4. `diamonds.csv`, a data file for Problem 2

### Problem 1: Polynomial Regression

A common misconception is that linear regression can only be used to fit a linear relationship. We can fit more complex relationships by defining new features.

A degree `d` polynomial is:

ŷ_d(x) = a_d x^d + a_(d−1)x^(d−1) + ... + a₁x + b

The parameters are:

β = (a_d, ..., a₁, b)^T

Examples:
- d = 1 → line
- d = 2 → quadratic
- d = 3 → cubic

In this problem you will:

1. Complete the functions in `polyfit.py`.

   This includes:
   - parsing the input data
   - creating the feature matrix
   - solving the least squares equations

2. Use your code to fit polynomials with degrees:

   d = 1, 2, 3, 4, 5

   using the dataset `poly.txt`.

3. Use `matplotlib.pyplot` to visualize:

   - the dataset
   - the fitted curves

   Plot `y`, `ŷ₁(x)`, `ŷ₂(x)`, `ŷ₃(x)`, `ŷ₄(x)`, `ŷ₅(x)` on the same graph.

   Make sure to:
   - use different colors
   - include a legend

   Then answer: **What degree polynomial seems to best fit the data? Explain.**

4. If a new datapoint is measured at:

   x = 2

   what is the predicted value `ŷ` using the best fitting polynomial?

Note: **You are not permitted to use sklearn for this problem.**  
You must use **numpy matrix operations** to solve the least squares equations.

Once completed, running the provided test case should output (rounded to 6 digits):

```
[[7.00158, 9.30386, -239.334],
 [0.00598796, 0.755218, 0.234560, 1.17636, -175.880]]
```

### Problem 2: Regularized Regression

Regularization techniques like **ridge regression** introduce a parameter `λ`.

To determine the best value of `λ`, we use **cross validation**.

You will use the `diamonds.csv` dataset containing roughly **54,000 diamonds** with attributes:

- carat
- cut
- color
- clarity
- depth
- table
- x
- y
- z
- price

Dataset source:

http://vincentarelbundock.github.io/Rdatasets/datasets.html

#### Tasks

1. Complete `normalize_train`

   Input: `X_train`

   Output:
   - normalized feature matrix
   - column means
   - column standard deviations

   Each column should have:

   mean = 0  
   std = 1

2. Complete `normalize_test`

   Input:

   - `X_test`
   - training means
   - training standard deviations

3. Define the lambda range:

   10^-1.00, 10^-0.97, 10^-0.94, ..., 10^1.97, 10^2.00

   Use:

```python
np.logspace()
```

   with `num = 101`.

4. Complete `train_model`

   Train a ridge regression model with parameter `λ = l`.

   Use:

```python
sklearn.linear_model.Ridge
```

5. Complete `error()`

   Compute **Mean Squared Error (MSE)**:

   MSE = average((y_pred − y_true)²)

6. In `main`, plot:

   **MSE vs λ**

   Include:
   - title
   - axis labels

   Determine the **best λ and best model**.

7. Write the final regression equation:

   ŷ(x) = a₁x₁ + a₂x₂ + ... + a₉x₉ + b

   Using the fitted model, predict the price for a diamond with:

   - 0.25 carat
   - cut = 3
   - color = 3
   - clarity = 5
   - depth = 60
   - table = 55
   - x = 4
   - y = 3
   - z = 2

Once completed, if you test with:

```
lambda = [1, 100]
```

you should see:

```
Best lambda tested is 1, which yields an MSE of 1812351.1908771885
```

## What to Submit

For each problem submit:

1. Your completed starter code
2. A writeup as a separate PDF

Files to submit:

- `polyfit.py`
- `problem1_writeup.pdf`
- `regularize-cv.py`
- `problem2_writeup.pdf`

## Submitting your Code

Push your completed files to your repository before the deadline.

Verify that the files appear correctly on GitHub.