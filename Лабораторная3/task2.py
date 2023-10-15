# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, split_char=','):
        first_set = set(participants_first_group.split(split_char))
        second_set = set(participants_second_group.split(split_char))
        common_list = list(first_set.intersection(second_set))
        return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
