import math
import time
import sympy
import sys


def log_operation(operation_name, inputs, result):
    try:
        with open("calculator.txt", "a") as f:
            f.write(f"Operation: {operation_name}\n")
            f.write(f"Inputs: {inputs}\n")
            f.write(f"Result: {result}\n")
            f.write("-" * 30 + "\n")

    except IOError as e:
        print(f"Warning: Could not write to log file: {e}")

    except Exception as e:
        print(f"Warning: Unexpected error while logging: {e}")


def show_menu():

    print('''
Scientific Calculator

0. Quit
1. Addition (+)
2. Subtraction (-)
3. Multiplication (x)
4. Division (/)
5. Mod (%)
6. n-th Root (ⁿ√x)
7. Power (^)
8. Absolute Value (|x|)
9. Factorial (n!)
10. Sinus (sin)
11. Cosinus (cos)
12. Tangent (tan)
13. Cotangent (cot)
14. Inverse Sinus (arcsin)
15. Inverse Cosinus (arccos)
16. Inverse Tangent (arctan)
17. Inverse Cotangent (arccot)
18. Natural Logarithm (ln)
19. Common Logarithm (log)
20. Exponential Function (exp(x))
21. Rounding Functions (round, floor, ceil)
22. Permutations (nPr)
23. Combinations (nCr)
24. Equation Solver (x = 0)
25. Derivatives (d/dx)
26. Integration (∫)
27. Matrix Calculations (A[])
          ---------------------------
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Transpose
          5. Determinant
          6. Trace
          7. Inverse Matrix
          ---------------------------
''')


def print_result(result):
    temp = "{:.6f}".format(result).rstrip('0').rstrip('.')
    print("Result = {}\n" .format(temp))


show_menu()
operator = input("Please enter your choice = ")  # string

while operator != '0':

    if operator == '1':
        try:
            x = float(input("Please enter the first number = "))
            y = float(input("Please enter the second number = "))
            result = x + y
            print_result(result)
            log_operation("Addition", f"num1 = {x}, num2 = {y}", result)

        except ValueError:
            print("\nError: Please enter valid numbers.\n")

    elif operator == '2':
        try:
            x = float(input("Please enter the first number = "))
            y = float(input("Please enter the second number = "))
            result = x - y
            print_result(result)
            log_operation("Subtraction", f"num1 = {x}, num2 = {y}", result)
        except ValueError:
            print("\nError: Please enter valid numbers.\n")

    elif operator == '3':
        try:
            x = float(input("Please enter the first number = "))
            y = float(input("Please enter the second number = "))
            result = x * y
            print_result(result)
            log_operation("Multiplication", f"num1 = {x}, num2 = {y}", result)
            
        except ValueError:
            print("\nError: Please enter valid numbers.\n")

    elif operator == '4':
        try:
            x = float(input("Please enter the first number = "))
            y = float(input("Please enter the second number = "))

            if y != 0:
                result = x / y
                print_result(result)
                log_operation("Division", f"num1 = {x}, num2 = {y}", result)

            else:
                print("\nDivision by zero is not possible.\n")

        except ValueError:
            print("\nError: Please enter valid numbers.\n")

    elif operator == '5':
        try:
            x = float(input("Please enter the first number = "))
            y = float(input("Please enter the second number = "))

            if y != 0 and x.is_integer() and y.is_integer():
                result = x % y
                print_result(result)
                log_operation("Mod", f"num1 = {x}, num2 = {y}", result)

            elif y == 0:
                print("\nModding by zero is not possible.\n")

            else:
                print("\nYou have to enter integers.\n")

        except ValueError:
            print("\nError: Please enter valid numbers.\n")

    elif operator == '6':
        try:
            print("Basic root function looks like -> ⁿ√x")
            n = float(input("Please enter the n value = "))
            x = float(input("Please enter the x value = "))

            if n == 0:
                print("\nRoot degree cannot be zero.\n")

            elif n.is_integer():
                if n % 2 == 1:
                    result = math.pow(x, 1/n)
                    print_result(result)
                    log_operation("n-th Root", f"n = {n}, x = {x}", result)

                elif n % 2 == 0:
                    if x >= 0:
                        result = math.pow(x, 1/n)
                        print_result(result)
                        log_operation("n-th Root", f"n = {n}, x = {x}", result)

                    else:
                        print("Negative numbers are not allowed if n is even.")

            else:
                if x >= 0 or n != int(n):
                    result = math.pow(x, 1/n)
                    print_result(result)
                    log_operation("n-th Root", f"n = {n}, x = {x}", result)

                else:
                    print("\nInvalid operation for negative number with fractional root.\n")

        except ValueError:
            print("\nError: Please enter valid numbers.\n")

        except ZeroDivisionError:
            print("\nError: Root degree cannot be zero.\n")

    elif operator == '7':
        try:
            x = float(input("Please enter the base number = "))
            y = float(input("Please enter the power number = "))
            result = math.pow(x, y)
            print_result(result)
            log_operation("Power", f"base = {x}, power = {y}", result)

        except ValueError:
            print("\nError: Please enter valid numbers.\n")
        except OverflowError:
            print("\nError: Result too large to calculate.\n")

    elif operator == '8':
        try:
            x = float(input("Please enter the number = "))
            result = abs(x)
            print_result(result)
            log_operation("Absolute Value", f"number = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '9':
        try:
            x = float(input("Please enter the number = "))

            if x >= 0 and x.is_integer():
                result = math.factorial(int(x))
                print_result(result)
                log_operation("Factorial", f"number = {x}", result)

            elif x >= 0:
                print("\nYou have to enter an integer.\n")

            else:
                print("\nNumber should be positive or zero.\n")

        except ValueError:
            print("\nError: Please enter a valid number.\n")
        except OverflowError:
            print("\nError: Number too large for factorial calculation.\n")

    elif operator == '10':
        try:
            x = float(input("Please enter the degree = "))
            y = math.radians(x)
            result = math.sin(y)
            print_result(result)
            log_operation("Sinus", f"degree = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '11':
        try:
            x = float(input("Please enter the degree = "))
            y = math.radians(x)
            result = math.cos(y)
            print_result(result)
            log_operation("Cosinus", f"degree = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '12':
        try:
            x = float(input("Please enter the degree = "))

            if x % 180 == 90:
                print("\ntan(x) is undefined.\n")

            else:
                y = math.radians(x)
                result = math.tan(y)
                print_result(result)
                log_operation("Tangent", f"degree = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '13':
        try:
            x = float(input("Please enter the degree = "))

            if x % 180 == 0:
                print("\ncot(x) is undefined.\n")

            else:
                y = math.radians(x)
                result = 1 / math.tan(y)
                print_result(result)
                log_operation("Cotangent", f"degree = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

        except ZeroDivisionError:
            print("\ncot(x) is undefined at this angle.\n")

    elif operator == '14':
        try:
            x = float(input("Please enter the value = "))

            if x >= -1 and x <= 1:
                result = math.asin(x)
                result = math.degrees(result)
                print_result(result)
                log_operation("Inverse Sinus", f"value = {x}", result)

            else:
                print("\nValue should be between -1 and 1.\n")

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '15':
        try:
            x = float(input("Please enter the value = "))

            if x >= -1 and x <= 1:
                result = math.acos(x)
                result = math.degrees(result)
                print_result(result)
                log_operation("Inverse Cosinus", f"value = {x}", result)

            else:
                print("\nValue should be between -1 and 1.\n")

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '16':
        try:
            x = float(input("Please enter the value = "))
            result = math.atan(x)
            result = math.degrees(result)
            print_result(result)
            log_operation("Inverse Tangent", f"value = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '17':
        try:
            x = float(input("Please enter the value = "))

            if x == 0:
                sol = 90
                print_result(sol)
                log_operation("Inverse Cotangent", f"value = {x}", sol)

            elif x > 0:
                result = math.atan(1/x)
                result = math.degrees(result)
                print_result(result)
                log_operation("Inverse Cotangent", f"value = {x}", result)

            elif x < 0:
                result = math.atan(1/x)
                result = math.degrees(result) + 180
                print_result(result)
                log_operation("Inverse Cotangent", f"value = {x}", result)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '18':
        try:
            print("Natural logarithm looks like -> log(e)(x)\n")
            x = float(input("Please enter the x value = "))

            if x > 0:
                result = math.log(x, math.e)
                print_result(result)
                log_operation("Natural Logarithm", f"value = {x}", result)

            else:
                print("\nArgument should be positive.\n")

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '19':
        try:
            print("Common logarithm looks like -> log(base)(x)\n")
            base = float(input("Please enter the base value = "))
            x = float(input("Please enter the x value = "))
            if base > 0 and x > 0 and base != 1:
                result = math.log(x, base)
                print_result(result)
                log_operation("Common Logarithm", f"base = {base}, value = {x}", result)
            else:
                print("\nBase should be positive, argument should be positive and base cannot be 1.\n")

        except ValueError:
            print("\nError: Please enter valid numbers.\n")

    elif operator == '20':
        try:
            print("Exponential function looks like -> num * exp(exponent)\n")
            num = float(input("Please enter the number value = "))
            exponent = float(input("Please enter the exponent value = "))
            result = num * math.exp(exponent)
            print_result(result)
            log_operation("Exponential Function", f"num = {num}, exponent = {exponent}", result)

        except ValueError:
            print("\nError: Please enter valid numbers.\n")
        except OverflowError:
            print("\nError: Result too large to calculate.\n")

    elif operator == '21':
        try:
            num = float(input("Please enter your number = "))

            result1 = math.floor(num)
            print("Floor result = {}".format(result1))
            log_operation("Rounding Functions (Floor)", f"num = {num}", result1)

            result2 = round(num)
            print("Round result = {}".format(round(num)))
            log_operation("Rounding Functions (Round)", f"num = {num}", result2)

            result3 = math.ceil(num)
            print("Ceil result = {}".format(math.ceil(num)))
            log_operation("Rounding Functions (Ceil)", f"num = {num}", result3)

        except ValueError:
            print("\nError: Please enter a valid number.\n")

    elif operator == '22':
        try:
            print("Number of ways to arrange r objects out of n distinct objects")
            n = float(input("Enter the n value = "))
            r = float(input("Enter the r value = "))

            if n.is_integer() and r.is_integer() and n >= 0 and r >= 0 and r <= n:
                n = int(n)
                r = int(r)
                result = math.perm(n, r)
                print_result(result)
                log_operation("Permutation", f"num1 = {n}, num2 = {r}", result)

            else:
                print("N and R should be integers, N must be positive or 0, R must be positive or 0 and less than N.")

        except ValueError:
            print("\nError: Please enter valid numbers.\n")
        except OverflowError:
            print("\nError: Result too large to calculate.\n")

    elif operator == '23':
        try:
            print("Number of ways to choose r objects from n distinct objects, order doesnt matter")
            n = float(input("Enter the n value = "))
            r = float(input("Enter the r value = "))

            if n.is_integer() and r.is_integer() and n >= 0 and r >= 0 and r <= n:
                n = int(n)
                r = int(r)
                result = math.comb(n, r)
                print_result(result)
                log_operation("Combination", f"num1 = {n}, num2 = {r}", result)

            else:
                print("N and R should be integers, N must be positive or 0, R must be positive or 0 and less than N.")

        except ValueError:
            print("\nError: Please enter valid numbers.\n")
        except OverflowError:
            print("\nError: Result too large to calculate.\n")

    elif operator == '24':
        try:
            x = sympy.symbols('x')
            print("Solve equations of the form f(x) = 0")
            equation_input = input("Enter the equation using 'x' as the variable: ")

            equation = sympy.sympify(equation_input)
            solution = sympy.solve(equation, x)
            print_result(solution)
            log_operation("Equation Solver", f"equation = {equation_input}", solution)

        except Exception as e:
            print(f"\nError: Unable to solve equation. Please check your syntax. {str(e)}\n")

    elif operator == '25':
        try:
            x = sympy.symbols('x')
            equation_input = input("Enter the equation using 'x' as the variable = ")
            pointx0 = float(input("Enter the x0 point to calculate = "))

            f = sympy.sympify(equation_input)
            deriv = sympy.diff(f, x)
            result = deriv.subs(x, pointx0).evalf()  # type: ignore
            print_result(result)
            log_operation("Derivative", f"equation = {equation_input}, point = {pointx0}", result)

        except ValueError:
            print("\nError: Please enter a valid number for x0.\n")
        except Exception as e:
            print(f"\nError: Unable to calculate derivative. Please check your syntax. {str(e)}\n")

    elif operator == '26':
        try:
            x = sympy.symbols('x')
            f = sympy.sympify(input("Enter the equation using 'x' as the variable = "))

            choice = input("Do you want definite integral? (y/n): ")

            if choice.lower() == 'y':
                a = float(input("Enter lower limit: "))
                b = float(input("Enter upper limit: "))
                result = sympy.integrate(f, (x, a, b)).evalf()
                print_result(result)
                log_operation("Integration", f"lower_limit = {a}, upper_limit = {b}, equation{f}", result)

            elif choice.lower() == 'n':
                result = sympy.integrate(f, x)
                print(result)
                log_operation("Integration", f"equation = {f}", result)

            else:
                print("\nUndefined operation..\n")

        except ValueError:
            print("\nError: Please enter valid numbers for limits.\n")
        except Exception as e:
            print(f"\nError: Unable to calculate integral. Please check your syntax. {str(e)}\n")

    elif operator == '27':
        try:
            print("You can perform your choice of matrix operations with this operator.")
            print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Transpose
    5. Determinant
    6. Trace
    7. Inverse Matrix
        """)

            operator2 = input("Enter the operator you want to use = ")

            def input_matrix(rows, cols, matrix_number=1):
                matrix = []
                print(f"Enter the elements of matrix {matrix_number}:")

                for i in range(rows):
                    row = list(map(float, input(f"Row {i+1}: ").split()))
                    if len(row) != cols:
                        raise ValueError(f"Row {i+1} must have exactly {cols} values.")
                    matrix.append(row)

                return matrix

            def matrix_addition(matrix1, matrix2):
                return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

            def matrix_subtraction(matrix1, matrix2):
                return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

            if operator2 in ['1', '2']:
                rows = int(input("Number of rows: "))
                cols = int(input("Number of columns: "))

                matrix1 = input_matrix(rows, cols, 1)
                matrix2 = input_matrix(rows, cols, 2)

                if operator2 == '1':
                    matrix_result = matrix_addition(matrix1, matrix2)
                    log_operation("Matrix Addition", f"matrix1 = {matrix1}, matrix2 = {matrix2}", matrix_result)

                elif operator2 == '2':
                    matrix_result = matrix_subtraction(matrix1, matrix2)
                    log_operation("Matrix Subtraction", f"matrix1 = {matrix1}, matrix2 = {matrix2}", matrix_result)

                for row in matrix_result:
                    print(row)

            elif operator2 == '3':
                rows1 = int(input("Number of rows for first matrix = "))
                cols1 = int(input("Number of cols for first matrix = "))

                matrix1 = input_matrix(rows1, cols1)

                rows2 = int(input("Number of rows for second matrix = "))
                cols2 = int(input("Number of cols for second matrix = "))

                matrix2 = input_matrix(rows2, cols2)

                matrix3 = []

                for i in range(rows1):
                    row = []

                    for j in range(cols2):
                        row.append(0)
                    matrix3.append(row)

                if cols1 != rows2:
                    print("Matrices are not suitable for multiplication.")

                else:
                    for i in range(rows1):
                        for j in range(cols2):
                            for k in range(rows2):
                                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

                for row in matrix3:
                    print(row)

                log_operation("Matrix Multiplication", f"matrix1 = {matrix1}, matrix2 = {matrix2}", matrix3)

            elif operator2 == '4':
                rows = int(input("Number of rows: "))
                cols = int(input("Number of columns: "))

                matrix = input_matrix(rows, cols)
                transpose = [[matrix[i][j] for i in range(rows)] for j in range(cols)]

                for row in transpose:
                    print(row)

                log_operation("Transpose", f"rows = {rows}, cols = {cols}, matrix = {matrix}", transpose)

            elif operator2 == '5':
                print("For the determinant operation, your matrix must be square.")
                size = int(input("Number of rows/columns: "))
                matrix = input_matrix(size, size)

                if len(matrix) != len(matrix[0]):
                    print("Error: Matrix must be square for determinant.")

                else:
                    matrix_sym = sympy.Matrix(matrix)
                    det = matrix_sym.det()
                    print_result(det)
                    log_operation("Determinant", f"size = {size}, matrix = {matrix}", det)

            elif operator2 == '6':
                print("For the trace operation, your matrix must be square.")
                size = int(input("Number of rows/columns: "))
                matrix = input_matrix(size, size)

                if len(matrix) != len(matrix[0]):
                    print("Error: Matrix must be square for trace.")

                else:
                    trace = sum(matrix[i][i] for i in range(size))
                    print_result(trace)
                    log_operation("Trace", f"size = {size}, matrix = {matrix}", trace)

            elif operator2 == '7':
                print("For the inverse matrix operation, your matrix must be square")
                size = int(input("Number of rows/columns: "))
                matrix = input_matrix(size, size)

                if len(matrix) != len(matrix[0]):
                    print("Error: Matrix must be square for inverse.")

                else:
                    matrix_sym = sympy.Matrix(matrix)
                    det = matrix_sym.det()
                    if det == 0:
                        print("Determinant is 0, cannot be inversed.")

                    else:
                        inv_matrix = matrix_sym.inv()
                        size = len(matrix)
                        inverse_matrix = []

                        for i in range(size):
                            row = []

                            for j in range(size):
                                row.append(0)
                            inverse_matrix.append(row)

                        for i in range(size):
                            for j in range(size):
                                inverse_matrix[i][j] = round(float(inv_matrix[i, j]), 3)

                        for row in inverse_matrix:
                            print(row)

                        log_operation("Inverse Matrix", f"Original = {matrix}", inverse_matrix)

            else:
                print("\nInvalid operator\n")

        except ValueError as e:
            print(f"\nError: Please enter valid numbers or check matrix dimensions. {str(e)}\n")
        except Exception as e:
            print(f"\nError: Matrix operation failed. {str(e)}\n")

    else:
        print("\nUndefined operation..\n")

    time.sleep(1)
    show_menu()
    operator = input("Please enter your choice = ")


print("\nThe program is closing...\n")
time.sleep(3)
sys.exit(0)
