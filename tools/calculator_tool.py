def calculator_tool(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation=="divide":
        if b==0:
            return "Cannot divide by zero"
        return a/b
    else:
        return "Unsupported operation"