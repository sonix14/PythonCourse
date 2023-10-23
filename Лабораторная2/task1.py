money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month_count = 0

while True:
    month_excesses = spend - salary
    if month_excesses > money_capital:
        break
    spend += (spend * increase)
    month_count += 1
    money_capital -= month_excesses

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
