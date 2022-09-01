n = int(input('Введите семизначное число'))
numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
           n % 10]
chet = 0
nechet = 0

for number in numbers:
    if number % 2 == 0:
        chet += 1
    else:
        nechet += 1
if chet > nechet:
    print(sum(numbers))
else:
    print(numbers[0] * numbers[2] * numbers[5])