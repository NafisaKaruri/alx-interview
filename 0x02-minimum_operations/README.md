# 0x02 Minimum Operations

This project involves calculating the minimum number of operations needed to achieve exactly `n` characters in a text file using only "Copy All" and "Paste" operations. The goal is to find an efficient solution using algorithmic concepts.

## Concepts & Resources

- **Dynamic Programming**: Breaking down the problem into simpler subproblems and building up the solution.
  - [Dynamic Programming (GeeksforGeeks)](https://www.geeksforgeeks.org/dynamic-programming/)
  
- **Prime Factorization**: Understanding prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number `n`.
  - [Prime Factorization (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86a85c65c6f9b99c2e9/intro-to-prime-factorization)
  
- **Code Optimization**: Approaching problems from an optimization perspective to find the most efficient solution.
  - [How to Optimize Python Code](https://realpython.com/tutorials/performance/)
  
- **Greedy Algorithms**: Approaching the problem by choosing the best option at each step.
  - [Greedy Algorithms (GeeksforGeeks)](https://www.geeksforgeeks.org/greedy-algorithms/)
  
- **Basic Python Programming**: Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
  - [Python Functions (Official Documentation)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## Function

### `minOperations(n)`

- **Prototype:**

  ```python
  def minOperations(n):
  ```

- **Parameters:**

  - `n` (int): The target number of characters.

- **Returns:**
  - An integer representing the minimum number of operations required to achieve exactly `n` characters.
  - If `n` is impossible to achieve, return 0.

- **Overview:**

  - The minOperations function employs prime factorization to determine the fewest number of operations needed to reach n H characters. By identifying and summing the prime factors of n, the function calculates the total operations required, where each prime factor corresponds to a "Copy All" or "Paste" operation.
- **Algorithm Efficiency:**

 - **Time Complexity**: \(O(\sqrt{n})\) - The function iteratively checks for prime factors up to the square root of `n`.
  - **Space Complexity**: \(O(1)\) - The function uses a constant amount of space regardless of the input size.

## Example Usage

To test the function, run the main.py file

```bash
./main.py
```
