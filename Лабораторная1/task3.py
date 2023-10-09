# TODO Найдите количество книг, которое можно разместить на дискете
full_size = 1.44 * 1024
pages = 100
strings = 50
chars = 25
one_char = 4 / 1024
print("Количество книг, помещающихся на дискету:", round(full_size/(pages*strings*chars*one_char)))
