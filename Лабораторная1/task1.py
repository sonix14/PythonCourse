numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
new_numbers = numbers
new_numbers[4] = 0
summ = sum(new_numbers)
count = len(new_numbers)
numbers[4] = summ/count
print("Измененный список:", numbers)
