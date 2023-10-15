# TODO Напишите функцию для поиска индекса товара
def find_index(item_list, needed_item):
    index = None
    for i in range(0, len(item_list)):
        if item_list[i] == needed_item:
            index = i
            break
    return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
