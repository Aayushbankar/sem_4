# Practical 2: Pandas Notes

## Pandas Basics

Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool, built on top of the Python programming language.

### Core Data Structures
1. **Series**: One-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). It's like a column in a table.
2. **DataFrame**: Two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). It's like a spreadsheet or SQL table.

### Data Import/Export
- **CSV**: `pd.read_csv()`, `df.to_csv()`
- **Excel**: `pd.read_excel()`, `df.to_excel()`
- **JSON**: `pd.read_json()`, `df.to_json()`

### Data Exploration
- `df.head()`: View first n rows.
- `df.tail()`: View last n rows.
- `df.info()`: Summary of DataFrame (columns, non-null counts, dtypes).
- `df.describe()`: Statistical summary of numerical columns (count, mean, std, min, max, percentiles).
- `df.shape`: Tuple representing dimensionality (rows, columns).
- `df.columns`: List of column names.

### Data Manipulation
- **Selection**:
    - `df['col_name']`: Select a column (Series).
    - `df.loc[label]`: Access a group of rows and columns by label(s).
    - `df.iloc[position]`: Access a group of rows and columns by integer position(s).
- **Filtering**: `df[df['col_name'] > value]`
- **Missing Data**:
    - `df.isnull()`: Detect missing values.
    - `df.dropna()`: Remove missing values.
    - `df.fillna(value)`: Fill missing values.
- **Grouping**: `df.groupby('col_name').mean()` - Split-Apply-Combine strategy.
