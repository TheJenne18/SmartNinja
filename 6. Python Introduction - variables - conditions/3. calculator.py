num_a = int(input("first number: "))
num_b = int(input("second number: "))
operator = input("Operator + or - or * or /: ")

if operator == "+":
    print("Solutions: " + str(num_a + num_b))
elif operator == '-':
    print("Solutions: " + str(num_a - num_b))
elif operator == '*':
    print("Solutions: " + str(num_a * num_b))
elif operator == '/':
    print("Solutions: " + str(num_a / num_b))
