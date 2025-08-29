def some_func(list1, list2):
    """ Написать функцию, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые есть только в одном из списков.
Пример ввода:
[1, 2, 3, 4], [3, 4, 5, 6]
Пример вывода:
[1, 2, 5, 6] """

    # unique_list = []
    #
    # for item1 in list1:
    #     if item1 not in list2:
    #         unique_list.append(item1)
    #
    # for item2 in list2:
    #     if item2 not in list1:
    #         unique_list.append(item2)
    # return unique_list
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))


list1 = [3, 4]
list2 = [3, 4, 5, 6]

print(some_func(list1, list2))