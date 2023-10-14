list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
list_count = len(list_players)
players_count = int(list_count / 2)
team1 = list_players[:players_count]
team2 = list_players[players_count:]
print(team1)
print(team2)
