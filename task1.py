# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = input('Введите число: ')
# sum_num = 0
# i = 0
# while i < len(number):
#     sum_num += int(number[i])
#     i += 1

# print(sum_num)

number = int(input('Введите число: '))
sum_num = 0

while number > 0:
    residue = number % 10
    sum_num += residue
    number //= 10
print(sum_num)