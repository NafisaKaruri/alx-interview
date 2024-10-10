# 0x01 Lockboxes

This project involves determining whether all locked boxes can be opened given a list of boxes and their corresponding keys. Each box may contain keys to other boxes, and the challenge is to navigate through these keys efficiently.

## Concepts and Resources

- **Lists and List Manipulation:** [Python Lists (Official Documentations)](https://docs.python.org/3/tutorial/datastructures.html)
- **Graph Theory Basics:** [Graph Theory (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)
- **Algorithm Complexity:** [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)
- **Recursion:** [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)
- **Queue and Stack:** [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)
- **Set Operations:** [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Function

### `canUnlockAll`
- **Prototype:**
  ```python
  def canUnlockAll(boxes):
  ```

- **Parameters:**
  - `boxes` (list of lists): Representing the boxes and the keys inside each box.

- **Returns:**
  - `True` if all boxes can be opened; otherwise, return `False`.

- **Overview:**
  - The `canUnlockAll` function implements a breadth-first search (BFS) approach to unlock all boxes. BFS is suitable here as it explores all possibilities level by level, ensuring that once a box is unlocked, all possible keys can be utilized efficiently.

- **Algorithm Efficiency**:
  - **Time Complexity**: \(O(n + k)\), where \(n\) is the number of boxes and \(k\) is the total number of keys across all boxes (keys can be duplicated).
  - **Space Complexity**: \(O(n)\), for storing the unlocked status and keys.

## Example Usage

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```
