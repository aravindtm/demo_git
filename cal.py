def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, **, % (or 'quit' to exit)")
    
    while True:
        try:
            # Get user input
            expression = input("\nEnter calculation (e.g., 5 + 3): ").strip()
            
            if expression.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Evaluate the expression
            result = eval(expression)
            print(f"Result: {result}")
            
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
        except (ValueError, SyntaxError):
            print("Error: Invalid input! Please enter a valid mathematical expression.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()

#comment
