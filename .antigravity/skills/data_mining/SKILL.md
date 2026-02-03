---
name: data_mining
description: Mining algorithms, SQL queries, data preprocessing, and warehousing concepts
---

# Data Mining Assistant

**Purpose:** Explain DM concepts, write SQL queries, and implement mining algorithms.

---

## Data Mining Process (CRISP-DM)

```
1. Business Understanding
        ↓
2. Data Understanding
        ↓
3. Data Preparation
        ↓
4. Modeling
        ↓
5. Evaluation
        ↓
6. Deployment
```

---

## Key Algorithms

### Classification
| Algorithm     | Concept                           | When to Use                |
| ------------- | --------------------------------- | -------------------------- |
| Decision Tree | Recursive splitting on attributes | Interpretable rules needed |
| ID3           | Uses Information Gain             | Categorical attributes     |
| C4.5          | Uses Gain Ratio                   | Mixed attributes           |
| CART          | Uses Gini Index                   | Binary splits              |

### Clustering
| Algorithm    | Concept                     | Parameters     |
| ------------ | --------------------------- | -------------- |
| K-Means      | Centroid-based partitioning | k (clusters)   |
| Hierarchical | Agglomerative/Divisive tree | Linkage method |
| DBSCAN       | Density-based clustering    | eps, minPts    |

### Association Rules
| Metric     | Formula               | Meaning                         |
| ---------- | --------------------- | ------------------------------- |
| Support    | P(A∩B)                | How often items appear together |
| Confidence | P(B\|A) = P(A∩B)/P(A) | How often rule is correct       |
| Lift       | Confidence/P(B)       | Improvement over random         |

---

## Data Warehouse Concepts

### Schema Types
| Schema    | Structure                     | Use Case           |
| --------- | ----------------------------- | ------------------ |
| Star      | Fact table + Dimension tables | Simple queries     |
| Snowflake | Normalized dimensions         | Storage efficiency |
| Galaxy    | Multiple fact tables          | Complex analysis   |

### OLAP Operations
| Operation  | Description                           |
| ---------- | ------------------------------------- |
| Roll-up    | Aggregate (city → state → country)    |
| Drill-down | Disaggregate (year → quarter → month) |
| Slice      | Select one dimension value            |
| Dice       | Select multiple dimension values      |
| Pivot      | Rotate cube axes                      |

---

## SQL Patterns for Mining

### Aggregation
```sql
SELECT category, COUNT(*), AVG(price)
FROM products
GROUP BY category
HAVING COUNT(*) > 10;
```

### Window Functions
```sql
SELECT product, sales,
       RANK() OVER (ORDER BY sales DESC) as rank
FROM sales_data;
```

---

## Preprocessing Steps

| Step              | Methods                          |
| ----------------- | -------------------------------- |
| Missing Values    | Mean/median imputation, deletion |
| Normalization     | Min-Max, Z-score                 |
| Encoding          | One-hot, Label encoding          |
| Outliers          | IQR method, Z-score threshold    |
| Feature Selection | Correlation, chi-square          |

---

## Explanation Rules

- Include both SQL and Python approaches
- Show entropy/Gini calculations step-by-step
- Draw schema diagrams for warehouse questions
- Explain algorithm choice rationale
- Provide sample datasets for examples
