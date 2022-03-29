try:
    answer = 1/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
# Use specific errors like ZeroDivisionError and ValueError when used Try/Except
# You can use "as error" ----> print(err) to print the specific type of error
except ValueError:
    print("Invalid input")
