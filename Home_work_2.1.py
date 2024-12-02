print("Привіт! Потрібно ввести 4-значне число!")
entr_num = int(input("Введіть 4-значне число: "))

first_num = entr_num // 1000
second_num = (entr_num % 1000) // 100
third_num = (entr_num % 100) // 10
fourth_num = entr_num % 10

print(first_num)
print(second_num)
print(third_num)
print(fourth_num)
