def arithmetic_arranger(expression, result=False):
    if len(expression) > 5:
        return "Error: Too many problems."
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for exp in expression:
        exp = exp.replace(" ", "")
        if "+" in exp:
            exp = exp.split("+")
            operator = "+"
        elif "-" in exp:
            exp = exp.split("-")
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."
        if not (exp[0].isdigit() and exp[1].isdigit()):
            return "Error: Numbers must only contain digits."
        if len(exp[0]) > 4 or len(exp[1]) > 4:
            return "Error: Numbers cannot be more than six digits."

        align = max([len(exp[0]), len(exp[1])]) + 2
        if result:
            res = str(eval(exp[0] + operator + exp[
                1]))
            line4 += res.rjust(
                align) + "    "
        line1 += exp[0].rjust(align) + "    "
        line2 += operator + exp[1].rjust(
            align - 1) + "    "
        line3 += "-" * (align) + "    "
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    arranged_string = "\n".join(
        [line1, line2, line3])
    if result:
        line4 = line4.rstrip()
        arranged_string += "\n" + line4 + "\n" + line3
    return arranged_string

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "1356 + 9965"], True))