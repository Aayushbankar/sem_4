---
name: comparison_table
description: Generate structured comparison tables for concepts, tools, and technologies
---

# Comparison Table Generator

**Purpose:** Create clear, structured comparison tables for any set of items.

---

## Table Formats

### Standard Comparison
```markdown
| Feature   | Option A | Option B | Option C |
| --------- | -------- | -------- | -------- |
| Feature 1 | Value    | Value    | Value    |
| Feature 2 | Value    | Value    | Value    |
| Best For  | Use case | Use case | Use case |
```

### Pros/Cons
```markdown
| Aspect | Pros        | Cons           |
| ------ | ----------- | -------------- |
| Item 1 | + Advantage | - Disadvantage |
| Item 2 | + Advantage | - Disadvantage |
```

### Detailed Breakdown
```markdown
| Criteria    | Option A | Option B | Winner |
| ----------- | -------- | -------- | ------ |
| Speed       | Fast     | Slow     | A      |
| Cost        | High     | Low      | B      |
| Ease        | Medium   | Easy     | B      |
| **Overall** | -        | -        | **B**  |
```

---

## Comparison Dimensions

| Domain     | Common Comparison Criteria                   |
| ---------- | -------------------------------------------- |
| Algorithms | Time complexity, space complexity, stability |
| Protocols  | Speed, reliability, overhead, use case       |
| Tools      | Features, cost, learning curve, ecosystem    |
| Languages  | Performance, syntax, ecosystem, use case     |
| Databases  | ACID, scalability, query type, consistency   |

---

## Generation Rules

1. **Identify comparison dimensions** before creating table
2. **Use consistent terminology** across rows
3. **Include "Best For" row** when applicable
4. **Highlight winner** if comparison is evaluative
5. **Keep cells concise** - one key point per cell
6. **Order rows by importance** - most critical first

---

## Output Format

```
## [Item A] vs [Item B] Comparison

**Context:** [When this comparison matters]

| Criteria | Item A | Item B |
| -------- | ------ | ------ |
| ...      | ...    | ...    |

**Summary:** [One-line takeaway]

**Choose A when:** [Condition]
**Choose B when:** [Condition]
```
