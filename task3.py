# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет 
# с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – 
# счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no


number = input('Введите шестизначное число: ') # в num должно попасть целое число

first_sum_num = 0
second_sum_num = 0

first_sum_num = int(number[0]) + int(number[1]) + int(number[2])
second_sum_num = int(number[-1]) + int(number[-2]) + int(number[-3])

if first_sum_num == second_sum_num:
    print('Билет счастливый!!!')
else:
    print('Вам не повезло(')
