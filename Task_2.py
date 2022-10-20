#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

listMassive = [2, 3, 4, 5, 6]

result_list = []

for i in range((len(listMassive)+1)//2):
     result_list.append(listMassive[i]*listMassive[len(listMassive)-1-i])
print(f'Произведение пар чисел = {result_list}')