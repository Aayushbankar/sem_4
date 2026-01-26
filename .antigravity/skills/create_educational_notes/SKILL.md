---
name: create_educational_notes
description: Detailed guidelines for generating high-quality, textbook-level educational notes.
---

# Skill: Code Educational Notes

This skill defines the standard for creating "Gold Standard" educational notes. These notes are NOT cheatsheets, NOT summaries, and NOT "tips for exams". They are deep, rigorous, self-contained educational resources suitable for mastering a subject.

## 1. Core Philosophy
*   **Depth over Brevity**: Do not simplify for the sake of brevity. Explain the *mechanism*, not just the *result*.
*   **Professional Tone**: Use academic, authoritative language. Avoid informalities like "Teacher's tips", "Gotchas", or "Cool tricks". Use "Note", "Critical Insight", or "Mathematical Formulation".
*   **Structure**: Follow the **Cornell Hybrid Method**:
    *   **Concept**: The core idea.
    *   **Definition**: The formal academic definition.
    *   **Elaboration**: The "Feynman Explanation" (Intuitive understanding).
    *   **Technical Detail**: The math/logic/code behind it.
    *   **Applications**: Real-world usage.

## 2. Formatting Standards

### A. Headers
Use strict hierarchy.
```markdown
# Unit X: [Title]
## 1. [Major Topic]
### 1.1 [Sub-topic]
#### A. [Specific Concept]
```

### B. Definitions
Always use blockquotes for formal definitions.
> **Definition**: A [concept] is a [category] that [differentiator].

### C. Tables
Use tables for *every* comparison.
| Feature        | Concept A | Concept B |
| :------------- | :-------- | :-------- |
| **Philosophy** | ...       | ...       |
| **Mechanism**  | ...       | ...       |

### D. Code
Code blocks must be commented to explain *why*, not just *what*.
```python
# We use a set for O(1) lookups, preventing the O(N) scan of a list
visited_nodes = set()
```

## 3. Required Sections for Every Unit
1.  **Introduction & Motivation**: Why do we learn this? (First Principles).
2.  **Core Theory**: The definitions, math, and logic.
3.  **Mechanism / Architecture**: How it works under the hood (e.g., Memory layout, Math derivation).
4.  **Practical Implementation**: Code or detailed procedural steps.
5.  **Critical Analysis**: Pros, Cons, Limitations, Complexity Analysis ($O(N)$).
6.  **Review Question Bank**: 5-10 deep conceptual questions (Short Answer & Long Answer).

## 4. Forbidden Patterns
*   ❌ "Topper's Note": Use "Key Insight".
*   ❌ "Viva Trap": Use "Common Misconception".
*   ❌ "Don't memorize this": Explain it so well they don't *need* to memorize.
*   ❌ Slang or Emoji-heavy headers.

## 5. Workflow
When asked to create notes:
1.  **Analyze Syllabus**: Map every keyword in the syllabus to a section.
2.  **Research**: Use `search_web` to find the formal definitions and industrial applications if not known.
3.  **Draft**: Write detailed sections.
4.  **Refine**: Ensure every paragraph adds value. Remove fluff.
