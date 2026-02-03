---
name: explain_code
description: Annotate and explain code line-by-line with execution flow and logic breakdown
---

# Code Explainer

**Purpose:** Explain code with line-by-line annotations, execution flow, and conceptual breakdown.

---

## Explanation Protocol

### 1. Overview
- What does this code do? (one sentence)
- What problem does it solve?
- Language/framework identification

### 2. Structure Analysis
- Break into logical sections
- Identify key functions/classes
- Map dependencies

### 3. Line-by-Line Annotation
- Every non-trivial line explained
- Variable purpose clarified
- Logic reasoning stated

### 4. Execution Flow
- Trace execution order
- Show control flow path
- Identify loops/recursion depth

### 5. Edge Cases & Gotchas
- Where could this fail?
- What inputs break it?
- Common bugs in similar code

---

## Output Format

```
## Overview
[One-line summary]

## Code Structure
[Section breakdown]

## Detailed Walkthrough

### Section: [Name]
```language
[Original code block]
```

| Line | Code   | Explanation    |
| ---- | ------ | -------------- |
| 1    | `code` | [What it does] |
| 2    | `code` | [What it does] |

## Execution Flow
[Step-by-step trace]

## Key Concepts Used
- [Concept 1]: [Brief explanation]
- [Concept 2]: [Brief explanation]

## Potential Issues
- [Edge case or gotcha]
```

---

## Language-Specific Notes

| Language    | Focus Areas                                  |
| ----------- | -------------------------------------------- |
| Python      | Indentation, list comprehensions, decorators |
| Java/Kotlin | OOP patterns, lifecycle, null safety         |
| SQL         | Joins, subqueries, aggregation order         |
| JavaScript  | Async/await, closures, this binding          |

---

## Rules

- Explain WHY, not just WHAT
- Assume reader knows syntax basics
- Highlight non-obvious logic
- Point out best practice violations
- Suggest improvements if relevant
