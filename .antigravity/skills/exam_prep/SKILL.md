---
name: exam_prep
description: Generate question banks, MCQs, short answers, and revision sheets for exam preparation
---

# Exam Preparation Generator

**Purpose:** Create exam-focused content including question banks, MCQs, and revision materials.

---

## Output Types

### 1. MCQ Bank
```
## MCQ Bank: [Topic]

**Q1.** [Question stem]
- (A) Option 1
- (B) Option 2
- (C) Option 3
- (D) Option 4

**Answer:** (X) — [One-line justification]
```

### 2. Short Answer Questions
```
## Short Answers: [Topic]

**Q1.** [Question] (2 marks)
**A:** [Concise answer in 2-3 lines]
```

### 3. Long Answer Questions
```
## Long Answers: [Topic]

**Q1.** [Question] (5-7 marks)
**A:**
- Point 1
- Point 2
- [Diagram if needed]
- Example
```

### 4. Revision Sheet
```
## Revision: [Topic]

### Key Terms
| Term | Definition       |
| ---- | ---------------- |
| X    | One-line meaning |

### Key Formulas
- Formula 1: [with when to use]

### Common Questions
1. [Likely exam question]

### Traps to Avoid
- [Common mistake]
```

---

## Question Distribution

| Marks | Type   | Expected Length        |
| ----- | ------ | ---------------------- |
| 1     | MCQ    | Single choice          |
| 2     | Short  | 2-3 lines              |
| 3     | Short  | 4-5 lines or list      |
| 5     | Medium | Half page              |
| 7     | Long   | Full page with diagram |

---

## Coverage Rules

- Cover all subtopics in a unit
- Include at least 1 numerical if applicable
- Include at least 1 diagram-based question
- Mix remember/understand/apply levels
- Include previous year pattern questions if known

---

## Quality Checks

- Every MCQ has exactly one correct answer
- Distractors are plausible but clearly wrong
- Mark allocation matches answer length
- Questions are unambiguous
- Cover edge cases students often miss
