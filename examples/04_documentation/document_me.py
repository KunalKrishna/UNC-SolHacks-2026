"""
Exercise 04 — Documentation Generation
========================================
These functions have NO documentation. Use Copilot to add docstrings.

Instructions:
  1. Place your cursor inside a function, on a new line after the "def" line.
  2. Type triple quotes: \"\"\"
  3. Let Copilot generate the docstring — press Tab to accept.
  4. Alternatively, select a function and ask Copilot Chat to document it.

Run: python examples/04_documentation/document_me.py
"""

import math


def merge_sort(arr):
    """
    Sort an array using the merge sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: A new sorted list.
    """

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    """
    Merge two sorted lists into one sorted list.

    Args:
        left (list): The left sorted list.
        right (list): The right sorted list.

    Returns:
        list: A new sorted list containing all elements from both input lists.
    """

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def binary_search(arr, target):
    """Perform binary search on a sorted array.

    Args:
        arr (list): The sorted list to search.
        target: The value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def is_prime(n):
    """Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def matrix_multiply(a, b):
    """Multiply two matrices.

    Args:
        a (list of lists): The first matrix.
        b (list of lists): The second matrix.

    Returns:
        list of lists: The product of the two matrices.

    Raises:
        ValueError: If the matrices have incompatible dimensions.
    """
    if len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    rows_a, cols_b = len(a), len(b[0])
    cols_a = len(a[0])
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


def caesar_cipher(text, shift, decrypt=False):
    """Apply Caesar cipher to a string.

    Args:
        text (str): The string to encrypt or decrypt.
        shift (int): The number of positions to shift each letter.
        decrypt (bool): If True, decrypt the string; otherwise, encrypt it.

    Returns:
        str: The encrypted or decrypted string.
    """
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points.

    Args:
        point1 (tuple): The first point as a tuple of coordinates.
        point2 (tuple): The second point as a tuple of coordinates.

    Returns:
        float: The Euclidean distance between the two points.

    Raises:
        ValueError: If the points have different numbers of dimensions.
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))


def flatten_dict(d, parent_key="", separator="."):
    """Flatten a nested dictionary.

    Args:
        d (dict): The dictionary to flatten.
        parent_key (str): The parent key for nested keys.
        separator (str): The separator for nested keys.

    Returns:
        dict: A flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{separator}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, separator).items())
        else:
            items.append((new_key, v))
    return dict(items)


# ---------------------------------------------------------------------------
# Quick verification
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Module functions work correctly:")

    assert merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    print("  ✓ merge_sort")

    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    print("  ✓ binary_search")

    assert is_prime(17) is True
    assert is_prime(4) is False
    print("  ✓ is_prime")

    assert matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    print("  ✓ matrix_multiply")

    assert caesar_cipher("Hello", 3) == "Khoor"
    assert caesar_cipher("Khoor", 3, decrypt=True) == "Hello"
    print("  ✓ caesar_cipher")

    assert abs(calculate_distance((0, 0), (3, 4)) - 5.0) < 0.01
    print("  ✓ calculate_distance")

    assert flatten_dict({"a": {"b": 1, "c": {"d": 2}}}) == {"a.b": 1, "a.c.d": 2}
    print("  ✓ flatten_dict")

    print("\nNow add docstrings to every function using Copilot!")
