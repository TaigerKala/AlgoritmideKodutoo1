
def add_item(list, item):
    list.append(item)
    return list

def delete_last(list):
    list.pop(-1)
    return list

list = [1923.213, 39492.923, 2394923.05, 2394923.0, 123.0]
item = 3


add_item(list, item)

print(list)

delete_last(list)

print(list)