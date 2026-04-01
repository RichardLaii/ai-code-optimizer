from optimizer import optimize_code

print("=== Code Optimizer ===")

while True:
    user_input = input("\nPaste your code (or type 'exit'): ")

    if user_input.lower() == "exit":
        break

    result = optimize_code(user_input)

    print("\n--- Optimization Suggestions ---\n")
    print(result)