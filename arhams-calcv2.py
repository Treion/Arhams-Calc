print(" ▄▄▄       ██▀███   ██░ ██  ▄▄▄       ███▄ ▄███▓  ██████     ▄████▄   ▄▄▄       ██▓     ▄████▄  ")
print("▒████▄    ▓██ ▒ ██▒▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒▒██    ▒    ▒██▀ ▀█  ▒████▄    ▓██▒    ▒██▀ ▀█  ")
print("▒██  ▀█▄  ▓██ ░▄█ ▒▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░░ ▓██▄      ▒▓█    ▄ ▒██  ▀█▄  ▒██░    ▒▓█    ▄ ")
print("░██▄▄▄▄██ ▒██▀▀█▄  ░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██   ▒   ██▒   ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░    ▒▓▓▄ ▄██▒")
print(" ▓█   ▓██▒░██▓ ▒██▒░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒▒██████▒▒   ▒ ▓███▀ ░ ▓█   ▓██▒░██████▒▒ ▓███▀ ░")
print(" ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░▓  ░░ ░▒ ▒  ░")
print("  ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░░ ░▒  ░ ░     ░  ▒     ▒   ▒▒ ░░ ░ ▒  ░  ░  ▒   ")
print("  ░   ▒     ░░   ░  ░  ░░ ░  ░   ▒   ░      ░   ░  ░  ░     ░          ░   ▒     ░ ░   ░        ")
print("      ░  ░   ░      ░  ░  ░      ░  ░       ░         ░     ░ ░            ░  ░    ░  ░░ ░      ")
print("                                                            ░                          ░        ")
print("                      Welcome to Arham's Calc V2")

first_run = True

while True:
    if not first_run:
        print("\n" * 12)

    print("")
    print("                  ╔════════════════════════════════╗")
    print("                  ║                                ║")
    print("                  ║   ADDITION        : 1          ║")
    print("                  ║   SUBSTRACTION    : 2          ║")
    print("                  ║   MULTIPLICATION  : 3          ║")
    print("                  ║   DIVISION        : 4          ║") 
    print("                  ║   EXIT PROGRAM    : exit       ║")                                               
    print("                  ║                                ║")
    print("                  ╚════════════════════════════════╝")
    print("")
    print("")

    task = input("Enter the task you want the calculator to do: ").lower()

    if task == "exit":
        print("Exiting the calculator. Goodbye!")
        break

    if task in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if task == "1":
                print("The addition is:", num1 + num2)
            elif task == "2":
                print("The subtraction is:", num1 - num2)
            elif task == "3":
                print("The multiplication is:", num1 * num2)
            elif task == "4":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("The division is:", "{:.2f}".format(num1 / num2))

        except ValueError:
            print("Invalid input. Please enter numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    else:
        print(" ")
        print("╔===============╗")
        print("║ INVALID INPUT ║")
        print("╚===============╝")

    delay_seconds = 0.45
    start_time = 0
    while start_time < delay_seconds * 10000000: #adjusting the multiplier to try and get 1.5 seconds.
        start_time += 1

    first_run = False