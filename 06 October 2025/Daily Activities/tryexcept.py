try:
    value=int(input("Enter a number: "))
    print(10/value)
except ValueError:
    print("You did not enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution finished")