# Practical 1: NumPy & Matplotlib Notes

## NumPy Basics

NumPy (Numerical Python) is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

### Key Concepts
- **ndarray**: The core data structure, an N-dimensional array.
- **Dimensions (Axes)**: The number of dimensions of the array (0 for scalar, 1 for vector, 2 for matrix).
- **Shape**: A tuple representing the size of the array in each dimension (e.g., `(3, 4)` for 3 rows and 4 columns).
- **Data Types (dtype)**: Arrays have a fixed data type (e.g., `int32`, `float64`).

### Common Operations
- **Creation**: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, `np.random.rand()`.
- **Indexing/Slicing**: Accessing elements like `arr[0, 1]` or slicing `arr[0:2, :]`.
- **Math**: Element-wise operations (`+`, `-`, `*`, `/`) and matrix multiplication (`np.dot` or `@`).
- **Statistics**: `np.mean()`, `np.std()`, `np.sum()`, `np.min()`, `np.max()`.
- **Shape Manipulation**: `reshape()`, `flatten()`, `transpose()`.

---

## Matplotlib Visualization

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

### Plot Types
1. **Line Plot**: `plt.plot(x, y)` - Good for continuous data or trends.
2. **Bar Chart**: `plt.bar(categories, values)` - Good for comparing quantities across categories.
3. **Scatter Plot**: `plt.scatter(x, y)` - Good for showing relationship/correlation between two variables.
4. **Histogram**: `plt.hist(data, bins)` - Good for visualizing data distribution.
5. **Pie Chart**: `plt.pie(sizes)` - Good for showing proportions of a whole.

### Customization
- **Titles & Labels**: `plt.title()`, `plt.xlabel()`, `plt.ylabel()`.
- **Legends**: `plt.legend()` (requires labels in plots).
- **Grid**: `plt.grid(True)`.
- **Colors & Styles**: Can be specified in plot functions (e.g., `color='red'`, `linestyle='--'`).
