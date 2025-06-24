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

---
### 🔹 Insertion Sort — Time Complexity: O(N²)

- **Idea:** Build the sorted part of the list one element at a time by inserting each element into its correct position.
- **Approach:**
  - Iterate through the list.
  - For each element, compare it to elements on its left and **insert it into the correct position** by swapping backward.
- Best Case: O(n)
  
> 💡 Think of it as *"taking cards in your hand one by one and inserting each into its right place among the already sorted cards."*

---
### 🔹 Merge Sort — Time Complexity: O(N log N)

- **Idea:** Divide the list into halves, sort them recursively, and then merge them back together.
- **Approach:**
  1. Recursively divide the list until single elements remain.
  2. Merge sorted halves using a helper function.
- **Space Complexity:** O(N) (due to new lists during merge)


> 💡 Think of it as *"dividing a problem into smaller parts, solving them, and merging the solutions."*

---

### 🔹 Quick Sort — Time Complexity: Avg O(N log N), Worst O(N²)

- **Idea:** Choose a pivot and partition the array into two halves:
  - Elements ≤ pivot go left
  - Elements > pivot go right
- Recursively sort the partitions.
- **Space Complexity:** O(log N) for in-place version (due to recursion)


> 💡 Think of it as *"breaking the list around a pivot and sorting both sides."*

---

### 🧠 Summary

| Algorithm       | Best Time | Avg Time   | Worst Time | Space     | Stable 
|----------------|-----------|------------|------------|-----------|--------
| Selection Sort | O(N²)     | O(N²)      | O(N²)      | O(1)      | ❌     
| Bubble Sort    | O(N)      | O(N²)      | O(N²)      | O(1)      | ✅     
| Insertion Sort | O(N)      | O(N²)      | O(N²)      | O(1)      | ✅    
| Merge Sort     | O(N log N)| O(N log N) | O(N log N) | O(N)      | ✅    
| Quick Sort     | O(N log N)| O(N log N) | O(N²)      | O(log N)⁽*⁾ | ❌   

