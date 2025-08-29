from typing import List

def func_polyndrom(list1: List[int]) -> List[int]:
    """Написать функцию, которая получает на вход список чисел и возвращает новый список,
    содержащий только числа, которые являются палиндромами.
Пример ввода:
[121, 123, 131, 34543]
Пример вывода:
[121, 131, 34543]"""
    list_final = []

    # for item in list1:
    #     tuple1 = str(item)
    #     tuple2 = tuple1[-1::-1]
    #     if tuple1 == tuple2:
    #         list_final.append(item)
    # return list_final
    # for i in list1:
    #     if str(i) == str(i)[::-1]:
    #         list_final.append(i)

    return [i for i in list1 if str(i) == str(i)[::-1]]


list1 = [553, 123, 123]
if __name__ == '__main__':
    print(func_polyndrom(list1))

# print(func_polyndrom(list1))




