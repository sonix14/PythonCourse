# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as file:
        data = json.load(file)
    summa = 0.0
    for dict_ in data:
        summa += dict_["score"] * dict_["weight"]
    return round(summa, 3)


print(task())
