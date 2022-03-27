numbers = [
[1, 2, 4, 8, 16],
[3, 5, 7, 9, 11],
[1, 2, 3, 4, 5],
[2]
]

print(numbers[2][4])

for row in numbers:
    for column in row:
        print(column)

result = 0
for int in range (0, 101):
    result = result + int
print(result)
