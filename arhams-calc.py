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

# this program is very bad, and can not perform complex calculations, but I will keep updating this
# thanks to Rubait sir for teaching me python!

print("")
print("             Welcome to my first python program: Arham's Calc")

while True:
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

    task = input("Enter the task you want the calculator to do: ")
    if task == "exit":
        print("Exiting the calculator. Goodbye!")
        break
    if task == "1":
        add1 = float(input("Enter a number: "))
        add2 = float(input("Enter another number: "))
        print("The addition of the two numbers are:", add1 + add2)
    elif task == "2":
        sub1 = float(input("Enter a number: "))
        sub2 = float(input("Enter another number: "))
        print("The subtraction of the two numbers are:", sub1 - sub2)
    elif task == "3":
        mul1 = float(input("Enter a number: "))
        mul2 = float(input("Enter another number: "))
        print("The multiplication of the two numbers are:", mul1 * mul2)
    elif task == "4":
        div1 = float(input("Enter a number: "))
        div2 = float(input("Enter another number: "))
        print("The division of the two numbers are:", div1 / div2)
    else:
        print("╔===============╗")
        print("║ INVALID INPUT ║")
        print("╚===============╝")
