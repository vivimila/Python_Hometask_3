#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


listMassive = list(map(int, input("Введите числа (через пробел):\n").split()))
#listMassive = [2, 3, 5, 6]

сondition = len(listMassive)//2 + 1 if len(listMassive) % 2 != 0 else len(listMassive)//2
new_list = [listMassive[i]*listMassive[len(listMassive)-i-1] for i in range(сondition)]

#ans = listMassive[::len(listMassive)-1]
print(new_list)