print(2**3)

def raise_power(base_number, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_number
    return result

print(raise_power(3, 4))

