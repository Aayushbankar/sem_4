---
name: quick_revision
description: Generate ultra-compressed bullet summaries for rapid last-minute revision
---

# Quick Revision Generator

**Purpose:** Create maximum-density revision notes for last-minute recall.

---

## Format Specification

### Structure
```
## [Topic]

### Core Facts
- Fact 1
- Fact 2

### Key Formulas
- Formula: meaning

### Mnemonics
- [Memory aid]

### Exam Traps
- [Common mistake]
```

---

## Compression Rules

| Rule                   | Example                                                |
| ---------------------- | ------------------------------------------------------ |
| One concept per bullet | `TCP = reliable, connection-oriented`                  |
| Formula + meaning      | `O(log n) = halving each step (binary search)`         |
| Contrast pairs         | `Stack = LIFO, Queue = FIFO`                           |
| Acronyms               | `ACID = Atomicity, Consistency, Isolation, Durability` |
| Pattern recognition    | `All ML: data → train → predict → evaluate`            |

---

## Density Targets

| Topic Size     | Target Lines  |
| -------------- | ------------- |
| Single concept | 3-5 bullets   |
| Unit/Chapter   | 15-25 bullets |
| Entire subject | 50-80 bullets |

---

## Must Include

1. **Definitions** - One-line precise
2. **Formulas** - With variable meanings
3. **Differences** - Between similar concepts
4. **Examples** - One canonical example per concept
5. **Numbers** - Key thresholds, limits, counts
6. **Traps** - Where marks are commonly lost

---

## Must Avoid

- Explanations (use teaching mode if needed)
- Full sentences where phrases work
- Redundant information
- Examples that require context
- Anything that needs re-reading

---

## Output Example

```
## Quick Revision: Classification Algorithms

### Core
- Decision Tree: splits on best attribute (Gini/Entropy)
- Random Forest: bagging + feature randomness
- KNN: majority vote of k nearest neighbors
- SVM: finds maximum margin hyperplane
- Naive Bayes: assumes feature independence

### Formulas
- Entropy: H = -Σ p log₂(p)
- Gini: 1 - Σ p²
- Accuracy: (TP+TN) / Total

### Traps
- KNN sensitive to k choice and scaling
- Naive Bayes fails with correlated features
- Decision Tree overfits without pruning
```
