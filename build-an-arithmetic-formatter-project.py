** start of main.py **

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    result_line = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."

        left, operator, right = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left), len(right)) + 2
        top = left.rjust(width)
        bottom = operator + right.rjust(width - 1)
        dash = '-' * width

        first_line.append(top)
        second_line.append(bottom)
        dash_line.append(dash)

        if show_answers:
            result = str(eval(left + operator + right))
            result_line.append(result.rjust(width))

    arranged = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dash_line)

    if show_answers:
        arranged += "\n" + "    ".join(result_line)

    return arranged


# Example run (this can be replaced with test cases)
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

** end of main.py **

