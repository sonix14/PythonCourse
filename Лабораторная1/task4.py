users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']


dict = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
dict["Общее количество"] = len(users)
new_set = set(users)
dict["Уникальные посещения"] = len(new_set)
print(dict)
