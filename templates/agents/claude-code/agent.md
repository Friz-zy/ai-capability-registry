---
name: custom-agent
description: >
  Use this agent when [triggering conditions].
  Examples:
  <example>
  Context: [Situation description]
  user: "[User request]"
  assistant: "[How assistant should respond]"
  <commentary>
  [Why this agent should be triggered]
  </commentary>
  </example>
model: inherit
color: blue
tools:
  - Read
  - Write
  - Grep
  - Bash
hidden: false
---

You are a specialized agent for [purpose].

**Your Core Responsibilities:**
1. [Responsibility 1]
2. [Responsibility 2]

**Analysis Process:**
[Step-by-step workflow]

**Output Format:**
[What to return]

**Constraints:**
- [Constraint 1]
- [Constraint 2]