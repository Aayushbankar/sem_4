# Practical 2: Data Engineering with Pandas

## 1. Introduction & Motivation
Real-world data is rarely clean. It contains missing values, inconsistent types, and noise. **Pandas** (Python Data Analysis Library) provides the data structures and operations necessary for **Data Wrangling**: the process of transforming raw data into a format suitable for analytics or machine learning.

## 2. Pandas Architecture

### 2.1 The Index: A Hash Map
The defining feature of Pandas `Series` and `DataFrame` is the **Index**.
*   **Structure**: The Index acts as a Hash Map (Entry $\to$ Row Location).
*   **Constraint**: While rows have integer positions (0 to N-1), they also have labels (Index).
*   **Implication**: Data Alignment. When performing operations ($A + B$), Pandas aligns data by **Index Label**, not by position. This prevents accidental mismatching of data (e.g., adding "Apple" price to "Orange" price just because they are in the same row).

### 2.2 Selection Logic: Set Theory
Understanding `.loc` vs `.iloc` requires set theory.

| Selector      | Domain                        | Range/Slice Logic               | Formal Definition                                                                |
| :------------ | :---------------------------- | :------------------------------ | :------------------------------------------------------------------------------- |
| **`.loc[]`**  | Labels ($L \in Index$)        | **Closed Interval** $[a, b]$    | Selects rows where $Index = L$. Slicing `['A':'C']` returns A, B, AND C.         |
| **`.iloc[]`** | Integers ($i \in \mathbb{Z}$) | **Half-Open Interval** $[a, b)$ | Selects rows at memory offset $i$. Slicing `[0:3]` returns 0, 1, 2 (Excludes 3). |

## 3. Data Wrangling Theory

### 3.1 Taxonomy of Missing Data
Handling `NaN` (Not a Number) depends on *why* the data is missing.
1.  **MCAR (Missing Completely at Random)**: No pattern. (e.g., a sensor battery died). $\to$ Safe to drop or simple impute.
2.  **MAR (Missing at Random)**: Missingness depends on observed data (e.g., Men are less likely to report "Depression" than Women). $\to$ Requires conditional imputation.
3.  **MNAR (Missing Not at Random)**: Missingness depends on the missing value itself (e.g., High-income earners hiding their salary). $\to$ Dropping introduces severe bias.

### 3.2 Imputation Strategies
Replacing missing values is an approximation of the underlying distribution.
*   **Mean Imputation**: $\hat{x} = \mu$. Preserves the mean but reduces variance (underestimates spread).
*   **Median Imputation**: Robust to outliers.
*   **Forward Fill**: $\hat{x}_t = x_{t-1}$. Valid only for time-series data (autocorrelation assumption).

## 4. Critical Analysis: Performance
Pandas is built on NumPy but adds overhead for index management.
*   **Copy-on-Write**: Historically, Pandas was aggressive about copying data. Modern versions (2.0+) are moving towards Copy-on-Write to improve memory efficiency.
*   **Chained Indexing**: `df['A'][0] = 5`.
    *   **Problem**: Python executes this as `get('A')` (returns temporary object) $\to$ `set(0)`. The modification happens on the temporary object and is lost.
    *   **Solution**: Atomic operation `df.loc[0, 'A'] = 5`.

## 5. Review Question Bank

### Short Answer
1.  Why is `.loc` slicing inclusive while `.iloc` slicing is exclusive?
2.  Explain the concept of "Data Alignment" in Pandas. What happens if you add two Series with different indices?
3.  Define MCAR and MNAR. Which one is "dangerous" to drop?

### Long Answer
1.  **Architecture**: Discuss the underlying data structure of a DataFrame. How does it manage columns of different data types (int, float, object) given that NumPy arrays must be homogeneous? (Hint: Block Manager).
2.  **Wrangling Pipeline**: You are given a dataset of Housing Prices with 20% missing values in the "Garage Area" column.
    *   If "Garage Area" is missing because the house has no garage, how should you handle it?
    *   If it is missing because of a recording error, how should you handle it?
    *   Write the Pandas code for both strategies.
