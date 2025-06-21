# DSA Practice

## ✅ Day 1: Sorting Algorithms

### 🔹 Selection Sort — Time Complexity: O(N²)

- **Idea:** Place the **minimum** element at the front in each iteration.
- **Approach:**
  - Iterate from index `i` to the end of the list.
  - Find the **minimum element** in the unsorted part.
  - Swap it with the element at index `i`.

> 💡 Think of it as *"selecting the smallest element and moving it to its correct position."*

---

### 🔹 Bubble Sort — Time Complexity: O(N²)

- **Idea:** Repeatedly "bubble up" the **maximum** element to the end.
- **Approach:**
  - Compare adjacent elements and swap if they are out of order.
  - After each pass, the largest element moves to its correct position at the end.
- Best Case: O(n)  

> 💡 Think of it as *"pushing the biggest element to the end like a bubble floating to the top."*

### 🔹 Insertion Sort — Time Complexity: O(N²)

- **Idea:** Build the sorted part of the list one element at a time by inserting each element into its correct position.
- **Approach:**
  - Iterate through the list.
  - For each element, compare it to elements on its left and **insert it into the correct position** by swapping backward.
- Best Case: O(n)
  
> 💡 Think of it as *"taking cards in your hand one by one and inserting each into its right place among the already sorted cards."*
