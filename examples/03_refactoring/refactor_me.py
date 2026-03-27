"""
Exercise 03 — Refactoring with Copilot
========================================
This code WORKS but is intentionally messy. Your job is to refactor it with
Copilot's help while keeping all the self-checks passing.

How to refactor:
  1. Select all code in this file.
  2. Open Copilot Chat (Ctrl+Shift+I).
  3. Ask: "Refactor this code to be more Pythonic, readable, and follow best
     practices. Keep the same function signatures and behavior."
  4. Review the suggestion and apply it.
  5. Run the self-checks to make sure nothing broke.

Run: python examples/03_refactoring/refactor_me.py

"""

from collections import Counter


# --- MESSY FUNCTION 1: Grade calculator ---

def g(s):
    """Calculate letter grade from numeric score."""
    grades = [
        (97, "A+"),
        (93, "A"),
        (90, "A-"),
        (87, "B+"),
        (83, "B"),
        (80, "B-"),
        (77, "C+"),
        (73, "C"),
        (70, "C-"),
        (60, "D"),
    ]
    for threshold, grade in grades:
        if s >= threshold:
            return grade
    return "F"


# --- MESSY FUNCTION 2: Statistics ---

def st(n):
    """Calculate statistics on a list of numbers."""
    if not n:
        return None
    
    sorted_n = sorted(n)
    mean = sum(n) / len(n)
    
    # Calculate median
    mid = len(sorted_n) // 2
    if len(sorted_n) % 2 == 0:
        median = (sorted_n[mid - 1] + sorted_n[mid]) / 2
    else:
        median = sorted_n[mid]
    
    return {
        "mean": mean,
        "median": median,
        "min": min(n),
        "max": max(n),
    }


# --- MESSY FUNCTION 3: FizzBuzz ---

def fb(n):
    """Generate FizzBuzz sequence up to n."""
    return [
        "FizzBuzz" if i % 15 == 0
        else "Fizz" if i % 3 == 0
        else "Buzz" if i % 5 == 0
        else str(i)
        for i in range(1, n + 1)
    ]


# --- MESSY FUNCTION 4: Word frequency counter ---

def wf(t):
    """Count word frequencies in text, sorted by frequency (descending)."""
    words = t.lower().split()
    # Keep only lowercase letters (a-z)
    cleaned = [
        "".join(c for c in word if "a" <= c <= "z")
        for word in words
    ]
    # Filter out empty strings
    cleaned = [word for word in cleaned if word]
    # Count and sort by frequency
    counter = Counter(cleaned)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


# ---------------------------------------------------------------------------
# SELF-CHECKS — Run this file to verify refactoring didn't break anything
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Running refactoring self-checks...\n")

    # Grade calculator checks
    assert g(98) == "A+"
    assert g(95) == "A"
    assert g(91) == "A-"
    assert g(88) == "B+"
    assert g(85) == "B"
    assert g(81) == "B-"
    assert g(78) == "C+"
    assert g(74) == "C"
    assert g(71) == "C-"
    assert g(65) == "D"
    assert g(55) == "F"
    print("  ✓ Grade calculator works!")

    # Statistics checks
    result = st([4, 1, 7, 3, 9])
    assert result["mean"] == 4.8
    assert result["median"] == 4
    assert result["min"] == 1
    assert result["max"] == 9
    assert st([]) is None
    print("  ✓ Statistics works!")

    # FizzBuzz checks
    result = fb(15)
    assert result[0] == "1"
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
    assert len(result) == 15
    print("  ✓ FizzBuzz works!")

    # Word frequency checks
    result = wf("the cat sat on the mat the cat")
    assert result[0] == ("the", 3)
    assert result[1] == ("cat", 2)
    print("  ✓ Word frequency works!")

    print("\n✅ All self-checks passed! Your refactoring didn't break anything.")
