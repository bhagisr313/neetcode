# NeetCode & LeetCode Practice

A structured collection of my **LeetCode problem-solving practice**, organized by topic and difficulty.

This repository is part of my ongoing preparation for **Data Structures & Algorithms**, technical interviews, and graduate-level Computer Science/Data Science studies.

---

## 📚 Repository Structure

Problems are organized according to their primary **NeetCode topic/pattern** and then separated by difficulty.

```text
neetcode/
│
├── l1_arrays_and_hashing/
│   ├── Easy/
│   └── Medium/
│
├── l2_stacks/
│   └── Easy/
│
├── l2_two_pointers/
│   └── Easy/
│
├── l3_binary_search/
│   ├── Easy/
│   └── Medium/
│
├── l3_linked_list/
│   └── Easy/
│
├── l3_sliding_window/
│   └── Easy/
│
├── l4_trees/
│   └── Easy/
│
├── l5_backtracking/
│   ├── Easy/
│   └── Medium/
│
├── leetcode_easy_problems/
└── leetcode_medium_problems/
```

### Difficulty Levels

| Level     | Description                                          |
| --------- | ---------------------------------------------------- |
| 🟢 Easy   | Fundamental concepts and patterns                    |
| 🟡 Medium | More complex problem-solving and pattern application |
| 🔴 Hard   | Advanced problems and optimization                   |

---

## 🧠 Topics Covered

### 1. Arrays & Hashing

Problems involving:

- Arrays
- Hash maps
- Hash sets
- Frequency counting
- Prefix sums
- Sorting
- String manipulation

### 2. Stacks

Problems involving:

- Stack operations
- Matching parentheses
- Monotonic stack concepts
- String processing

### 3. Two Pointers

Problems involving:

- Two-pointer traversal
- In-place array manipulation
- String comparison
- Palindromes
- Sorted arrays

### 4. Binary Search

Problems involving:

- Classic binary search
- Search space reduction
- Sorted arrays
- Matrix searching
- Numerical search

### 5. Linked Lists

Problems involving:

- Traversal
- Reversal
- Fast and slow pointers
- Cycle detection
- Merging linked lists

### 6. Sliding Window

Problems involving:

- Fixed-size windows
- Dynamic windows
- Subarrays
- String windows
- Optimization using window state

### 7. Trees

Problems involving:

- Binary trees
- Binary search trees
- DFS
- BFS
- Tree traversal
- Recursion
- Tree depth and balance

### 8. Backtracking

Problems involving:

- Recursion
- Subsets
- Combinations
- Decision trees
- Exploring possible solutions

---

## 📝 Solution Structure

Each Python file contains my solution to an individual LeetCode problem.

Typical filename format:

```text
pXXXX_problem_name.py
```

For example:

```text
p0001_two_sum.py
p0049_group_anagrams.py
p0074_search_a_2D_matrix.py
```

The problem number and title make it easy to identify the original LeetCode problem.

---

## 🔗 Related Easy Problems

Some Medium problems build directly on concepts introduced by easier problems.

For example:

```text
Group Anagrams
        ↓
Valid Anagram
```

```text
Top K Frequent Elements
        ↓
Contains Duplicate
```

```text
Product of Array Except Self
        ↓
Contains Duplicate
```

```text
Search a 2D Matrix
        ↓
Binary Search
```

These relationships are included in the corresponding Medium solutions as a reminder to review the simpler pattern when needed.

---

## 🛠️ Repository Organizer

This repository includes a Python organizer script:

```text
main.py
```

The organizer:

- Detects LeetCode problems from filenames
- Identifies their difficulty
- Creates `Easy` and `Medium` folders inside each topic
- Moves solutions into the appropriate difficulty folder
- Protects existing generic Easy/Medium folders
- Adds related Easy-problem references to selected Medium solutions
- Supports a safe **dry-run mode**

### Dry Run

Before moving any files, keep:

```python
DRY_RUN = True
```

This previews the changes without modifying the repository.

After confirming the output, change it to:

```python
DRY_RUN = False
```

Then run:

```bash
python main.py
```

> Always use dry-run mode first when changing the repository structure.

---

## 📊 Current Progress

The repository currently contains solutions across the following areas:

- Arrays & Hashing
- Stacks
- Two Pointers
- Binary Search
- Linked Lists
- Sliding Window
- Trees
- Backtracking

### Current Problem Count

**113 problems detected and organized**

| Difficulty |   Count |
| ---------- | ------: |
| Easy       |      89 |
| Medium     |      24 |
| Hard       |       0 |
| **Total**  | **113** |

> This section should be updated as new problems are added.

---

## 🎯 Study Approach

My goal is not just to solve problems, but to understand the **patterns behind them**.

For each problem, I aim to understand:

1. What is the problem asking?
2. What pattern does it use?
3. What is the brute-force approach?
4. Can the solution be optimized?
5. What is the time complexity?
6. What is the space complexity?
7. Can I recognize the same pattern in another problem?

The focus is on **understanding and pattern recognition rather than memorizing solutions**.

---

## 🚀 Learning Progression

The general progression I am following is:

```text
Arrays & Hashing
        ↓
Two Pointers
        ↓
Sliding Window
        ↓
Stack
        ↓
Binary Search
        ↓
Linked List
        ↓
Trees
        ↓
Backtracking
        ↓
More Advanced Patterns
```

As my fundamentals improve, I will add additional topics such as:

```text
Heap / Priority Queue
Intervals
Greedy
Graphs
Dynamic Programming
Tries
Advanced Graph Algorithms
```

---

## 💻 Language

Primary programming language:

**Python**

The solutions are written with an emphasis on:

- Readability
- Simplicity
- Correctness
- Time complexity
- Space complexity
- Understanding reusable patterns

---

## 📈 Goals

- [x] Build a structured LeetCode repository
- [x] Organize problems by topic
- [x] Separate problems by difficulty
- [x] Build strong fundamentals
- [ ] Complete core NeetCode patterns
- [ ] Increase Medium problem coverage
- [ ] Start solving Hard problems
- [ ] Improve solution optimization
- [ ] Practice timed interview-style problems
- [ ] Review previously solved problems regularly

---

## 🔄 Review Strategy

Previously solved problems should not be considered permanently completed.

I plan to revisit problems that:

- Took significant time to solve
- Required hints
- Were solved with an inefficient approach
- Introduced a new pattern
- Are commonly useful in technical interviews

The goal is to eventually recognize the underlying pattern quickly rather than starting from scratch every time.

---

## 📌 Notes

This repository is primarily a **learning and practice repository**.

Solutions may evolve over time as I learn better approaches, improve code quality, or discover more efficient algorithms.

The objective is continuous improvement in:

**Problem Solving → Algorithms → Data Structures → Pattern Recognition → Interview Readiness**

---

## 🌱 Progress Over Perfection

The purpose of this repository is to document the learning process.

Every solved problem is one more opportunity to understand a pattern, make a mistake, improve the solution, and become a better problem solver.
