while True: 
    operand1 = float(input("\nMasukkan operand 1\t\t: "))
    operator = input("Masukkan operator (+, -, *, /)  : ")
    operand2 = float(input("Masukkan operand 2\t\t: "))

    if operator == '+':
            hasil = operand1 + operand2
    elif operator == '-':
            hasil = operand1 - operand2
    elif operator == '*':
            hasil = operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            hasil = operand1 / operand2
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print("Error: Operator tidak dikenal.")
        
    print(f"\n{operand1} {operator} {operand2} = {hasil}")