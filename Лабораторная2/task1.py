money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month_budget = salary + money_capital - spend
month_count = 1
month_budget += salary

while spend < month_budget:
    spend += (spend * increase)
    month_budget -= spend
    month_budget += salary
    month_count += 1

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
