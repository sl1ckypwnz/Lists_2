n = int(input("Сколько чисел в списке?"))
tmp = list(map(int, input("Целые числа,ввод через пробел ").split())) 
tmp.insert(0, tmp.pop())
print("Результат -", tmp) 