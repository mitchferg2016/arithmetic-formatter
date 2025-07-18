# Arithmetic Formatter – FreeCodeCamp Python Certification Project

This project is part of the [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) on freeCodeCamp.

## 🚀 Challenge Summary

The task was to create a Python function called `arithmetic_arranger()` that takes a list of arithmetic problems (using `+` and `-` only) and returns a neatly formatted string with the problems arranged vertically and side-by-side. Optionally, the function can also display the answers.

The data provided was this: 

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

I needed my .py script to create this output:
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    ----
  40     -3800     19998      474

## 🧠 Key Constraints

- Only addition and subtraction are allowed.
- Max of 5 problems per call.
- Numbers must contain only digits and be ≤ 4 digits long.
- Output must have proper spacing and alignment.
- Answers shown only when a second argument (`show_answers=True`) is passed.

## 🧰 Steps Taken to Solve the Challenge

1. Parsed each problem and split it into left number, operator, and right number.
2. Added validation for number length, digit-only input, and valid operators.
3. Used string formatting (`rjust`) to align numbers and dashes properly.
4. Constructed the 3 mandatory output lines (top, bottom, dashes).
5. Optionally calculated and added the fourth line for answers.
6. Joined all lines with consistent 4-space gaps between problems.
7. Returned the final formatted string for display.

---

✅ This project passed all test cases on freeCodeCamp and was submitted as part of the certification curriculum.

---

> **Files included:**
> - `build-an-arithmetic-formatter-project.py` — executable Python script
> - `build-an-arithmetic-formatter-project.txt` — exported copy from freeCodeCamp editor

