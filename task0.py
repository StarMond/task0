import random

# генерування списку з 30 чисел з -100 до 100   
arrayRand = random.sample(range(-100, 100), 30)
print("\n")

print("Сформувати список з 30 випадкових чисел:",arrayRand)

# Максимальний елемент списку
print("\nМаксимальний елемент списку: ") 
print(max(arrayRand)) 
# Порядковий номер максимального елементу списку
print("Порядковий номер: ") 
print(arrayRand.index(max(arrayRand)))

listForSort = [i for i in arrayRand if (i % 2) == 1]
if len(listForSort) == 0: 
    print("Непарних чисел не знайдено") 
print(sorted(listForSort, reverse=True)) 
print("\n")