# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    letters_dict = {}
    count = 0
    for char in text:
        if char.isalpha() and char not in letters_dict:
            for char_ in text:
                if char == char_:
                    count += 1
            letters_dict[char] = count
            count = 0
    return letters_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict):
    sum_count = sum(letter_dict.values())
    dict = {}
    for char, count in letter_dict.items():
        dict[char] = count / sum_count
    return dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letters_dict = count_letters(main_str)
dict = calculate_frequency(letters_dict)
for key, value in dict.items():
    print(f"{key}: {value:.2f}")
