# Practical 1: Numerical Computing Architecture

## 1. Introduction & Motivation
Machine Learning algorithms rely heavily on Linear Algebra (matrix multiplication, vector addition) and Calculus (gradients). Standard Python `list` structures are designed for general-purpose computing and are computationally inefficient for dense mathematical operations. **NumPy** solves this by providing C-level optimized arrays, while **Matplotlib** offers data visualization tools essential for Exploratory Data Analysis (EDA).

## 2. NumPy Architecture

### 2.1 The Need for Speed: Python Lists vs. NumPy Arrays
Why is NumPy 50x-100x faster than Python lists?
1.  **Memory Layout**:
    *   **Python List**: An array of pointers to objects scattered across the heap. Iterating requires pointer dereferencing and type checking for every element ($O(N)$ overhead).
    *   **NumPy Array (`ndarray`)**: A contiguous block of homogeneous memory (e.g., all `int64`). The CPU can load entire cache lines of data at once, minimizing cache misses.
2.  **SIMD (Single Instruction, Multiple Data)**:
    *   Modern CPUs can execute one instruction on multiple data points simultaneously (Vectorization). NumPy leverages these hardware instructions.

### 2.2 Mathematical Concept: Broadcasting
Broadcasting is the set of rules that allows binary operations (e.g., addition) on arrays of different shapes.
> **Definition**: Two dimensions are compatible when:
> 1. They are equal, or
> 2. One of them is 1.

#### Visualizing Mechanics
Consider Matrix $A$ $(3 \times 3)$ and Vector $b$ $(3, 1)$:
$$
A = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}, \quad b = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
$$
Operation $A + b$:
NumPy "stretches" (broadcasts) $b$ horizontally to match $A$:
$$
\begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 3 & 3 & 3 \end{bmatrix} = \begin{bmatrix} 2 & 2 & 2 \\ 3 & 3 & 3 \\ 4 & 4 & 4 \end{bmatrix}
$$

### 2.3 Memory Management: Views vs. Copies
In NumPy, slicing often returns a **View** (reference to existing memory) rather than a Copy.
*   **Motivation**: To avoid duplicating gigabytes of data.
*   **Implication**: Modifying a slice modifies the original array.
```python
original = np.array([1, 2, 3])
view = original[0:2]
view[0] = 99
# 'original' is now [99, 2, 3]!
```
**Correctness Constraint**: Use `.copy()` explicitly when independence is required.

## 3. Matplotlib Architecture

### 3.1 The Object Hierarchy
Successful plotting requires understanding the object model, not just copy-pasting code.
1.  **Figure (`fig`)**: The top-level container (The "Canvas"). It holds all plot elements.
2.  **Axes (`ax`)**: The region where data is plotted (The "Graph"). A Figure can contain multiple Axes.
3.  **Axis**: The number-line objects (x-axis, y-axis) handling limits and ticks.

### 3.2 State-Machine vs. Object-Oriented Interface
*   **Pyplot (State-Machine)**: `plt.plot()`. Implicitly targets the "current" figure. Simple but dangerous for complex scripts.
*   **Object-Oriented (Recommended)**: `fig, ax = plt.subplots()`. Explicitly targets a specific Axes object. This is the industry standard for reproducible code.

## 4. Review Question Bank

### Short Answer
1.  Explain why iterating over a Python list is slower than a NumPy vectorized operation in terms of CPU cache and type checking.
2.  Given Array A of shape `(4, 1)` and Array B of shape `(4,)`, are they broadcastable? If so, what is the resulting shape?
3.  What is the difference between a Figure and an Axes in Matplotlib?

### Long Answer
1.  **Memory Architecture**: Describe how NumPy handles memory for a slice `arr[::2]` (step 2). Does it copy data? How does it map indices to memory addresses? (Hint: Strides).
2.  **Implementation**: Write a NumPy snippet to normalize a $(100 \times 5)$ matrix $X$ (subtract mean, divide by std dev) per column, without using any `for` loops. Explain how broadcasting makes this possible.
