import sys

username = input("Enter Username: ")
password = input("Enter Password: ")

if username.isalpha() and len(username) == 6 and "SWUSTCST" in password:
    print("\nLogin Successful!\n")
else:
    print("Invalid Username or Password!")
    sys.exit()


while True:

    print("\nEnter three numbers")

    try:
        a = int(input("Enter First number (positive only): "))
        b = int(input("Enter Second number (positive only): "))
        c = int(input("Enter Third number (positive only): "))
    except:
        print("Error! Only numbers are allowed.")
        continue

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid input! Only positive numbers allowed.")
        continue

    nums = sorted([a, b, c])

    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print("These numbers FOLLOW Pythagorean rule.")
    else:
        print("These numbers DO NOT follow Pythagorean rule.")

    print("\nWhat do you want to do?")
    print("1. Check again")
    print("2. Close program")

    choice = input("Enter choice: ")

    if choice == "1":
        continue
    else:
        print("Program closed.")

        break
