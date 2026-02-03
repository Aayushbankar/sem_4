---
name: create_practical_report
description: Generate formatted practical/lab reports with aim, theory, code, output, and conclusions
---

# Practical Report Generator

**Purpose:** Create complete, submission-ready lab practical reports.

---

## Report Structure

### Standard Format

```markdown
# Practical No. [X]

## Title
[Practical title]

## Aim
[One-line objective]

## Theory
[Relevant concepts - 3-5 sentences max]

## Algorithm / Steps
1. Step one
2. Step two
...

## Code
```language
[Complete working code]
```

## Output
[Console output or screenshot description]

## Conclusion
[What was learned - 1-2 sentences]
```

---

## Section Guidelines

| Section    | Length       | Content                 |
| ---------- | ------------ | ----------------------- |
| Aim        | 1 line       | Verb-first objective    |
| Theory     | 50-100 words | Core concepts only      |
| Algorithm  | 5-10 steps   | High-level procedure    |
| Code       | Complete     | Commented, working      |
| Output     | Varies       | Actual execution result |
| Conclusion | 1-2 lines    | Learning outcome        |

---

## Subject-Specific Templates

### FML (Machine Learning)
- Include: Dataset description, Libraries used, Accuracy metrics
- Output: Model performance, plots if applicable

### MAD (Android Development)
- Include: XML layout + Kotlin/Java code
- Output: Screenshot description or UI state

### CSDF (Cybersecurity)
- Include: Tool commands, Environment setup
- Output: Command results, findings

### DM (Data Mining)
- Include: SQL queries or preprocessing steps
- Output: Query results, patterns found

---

## Rules

- Code must be complete and runnable
- No placeholder comments like "// add your code here"
- Theory must be exam-relevant, not textbook copy
- Output must match the actual code execution
- Include any error handling if required by practical
