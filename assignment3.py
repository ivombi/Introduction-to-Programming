# Import libraries
import sys

def has_numbers(in_list):
    return any(char.isdigit() for char in in_list)


def check_brackets(expr):
    if expr.count("(") == expr.count(")"):
        return True
    else:
        return False


def check_operands(expr):
    # Define list of operators
    math_operators = ['*', '/', '%', '^', '+', '-']

    if not any([operator in expr for operator in math_operators]):
        return False

    for op in math_operators:
        if op in expr:
            exp_list = expr.split(op)
            for x in exp_list:
                if not has_numbers(x):
                    return False

    return True


#
def chalc(input_list=""):
    """
    """
    error = 0

    if len(input_list) >= 1:  # Check if there was an input
        #input_list = input_list.split()
        for expr in input_list:
            try:
                result_brack = check_brackets(expr)
                res_op = check_operands(expr)
                if all([result_brack, res_op]):
                    pass
                else:
                    print(expr)
                    error = error + 1

            except:
                print(expr)
                pass

    else:
        print("no input provided")

    if (len(input_list) >= 1) & (error < 1):
        print("correct")


# Access command line arguments
input_list = sys.argv[1:]

# Call function with command line arguments
chalc(input_list)