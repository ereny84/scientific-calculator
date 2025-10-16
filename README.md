# 🧮 Scientific Calculator

A comprehensive scientific calculator built with Python that supports advanced mathematical operations including calculus, linear algebra, and more.

## ✨ Features

### Basic Operations
- ➕ Addition, Subtraction, Multiplication, Division
- 🔢 Modulo operations
- 📊 Absolute value
- 🔢 Factorial calculations

### Advanced Mathematics
- 🔺 Trigonometric functions (sin, cos, tan, cot)
- 🔄 Inverse trigonometric functions (arcsin, arccos, arctan, arccot)
- 📈 Logarithmic functions (natural log, common log)
- ⚡ Exponential functions
- 🌟 Power and root calculations

### Calculus & Analysis
- 📐 Derivatives calculation
- ∫ Integration (definite and indefinite)
- 🎯 Equation solving
- 🔢 Permutations and combinations

### Linear Algebra
- ➕ Matrix addition and subtraction
- ✖️ Matrix multiplication
- 🔄 Matrix transpose
- 📊 Determinant calculation
- 🎯 Matrix trace
- ↩️ Matrix inverse

### Additional Features
- 📝 Operation logging to file
- 🛡️ Comprehensive error handling
- 🎨 User-friendly menu interface
- 📋 Mathematical input validation

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/ereny84/scientific-calculator.git
cd scientific-calculator
```

2. Install required dependencies:
```bash
pip install sympy
```

3. Run the calculator:
```bash
python calculator.py
```

## 📋 Requirements

- Python 3.7+
- sympy library
- math (built-in)
- sys (built-in)
- time (built-in)

## 🎯 Usage

Run the program and select from 27 different mathematical operations:

```
Scientific Calculator

0. Quit
1. Addition (+)
2. Subtraction (-)
3. Multiplication (x)
4. Division (/)
5. Mod (%)
...
27. Matrix Calculations
```

All operations are logged to `calculator.txt` for history tracking.

## 🛡️ Error Handling

The calculator includes comprehensive error handling for:
- Invalid number inputs
- Division by zero
- Domain errors (e.g., negative numbers in even roots)
- Matrix dimension mismatches
- Overflow errors for large calculations

## 📁 Files

- `calculator.py` - Main calculator program
- `calculator.txt` - Operation history log
- `README.md` - This documentation

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📄 License

This project is open source and available under the MIT License.

---
*Created by Eren Yildirim - Scientific Calculator Project*