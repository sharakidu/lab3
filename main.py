name = input("Enter your name: ").strip().capitalize()
lastname = input("Enter your lastname: ").strip().capitalize()
if name:
    print(f"Hello, {name, lastname} ")
else:
    print("Hello, World")
if name == "Ilya":
    print("Have a nice day!")