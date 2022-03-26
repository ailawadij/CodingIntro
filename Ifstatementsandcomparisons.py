def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num3 and num2>= num1:
        print(num2)
    else:
        return(num3)
print(max_num(23, 423, 901))
