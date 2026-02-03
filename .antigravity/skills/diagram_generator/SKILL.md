---
name: diagram_generator
description: Create Mermaid diagrams for visualizing concepts, flows, and architectures
---

# Diagram Generator

**Purpose:** Create clear, structured diagrams using Mermaid syntax.

---

## Diagram Types

### 1. Flowchart
```mermaid
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
```

### 2. Sequence Diagram
```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    C->>S: Request
    S-->>C: Response
```

### 3. Class Diagram
```mermaid
classDiagram
    class ClassName {
        +attribute: Type
        +method(): ReturnType
    }
    ClassName1 <|-- ClassName2 : Inheritance
```

### 4. Entity Relationship
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
```

### 5. State Diagram
```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> State2 : event
    State2 --> [*]
```

---

## Usage Guidelines

| Concept Type      | Recommended Diagram |
| ----------------- | ------------------- |
| Process/Algorithm | Flowchart           |
| Communication     | Sequence            |
| OOP Structure     | Class Diagram       |
| Database Schema   | ER Diagram          |
| State Machine     | State Diagram       |
| Timeline          | Gantt               |
| Hierarchy         | Mindmap             |

---

## Syntax Rules

- Node text with special chars: Use quotes `["Text (with parens)"]`
- Avoid HTML in labels
- Use descriptive node IDs
- Keep labels concise
- Use subgraphs for grouping

---

## Output Format

```
## [Concept Name] Diagram

[Brief description of what the diagram shows]

```mermaid
[diagram code]
```

**Key Points:**
- [Interpretation point 1]
- [Interpretation point 2]
```
