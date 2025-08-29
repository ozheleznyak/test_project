from typing import List

def test1(list1: List[int], list2: List[int]) -> List[int]:
    """ которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые встречаются в обоих списках """
    list3 = []

    for item in list1:
        if item in list2:
            list3.append(item)
    #return [i for i in list1 if i in list2 ] - краткая запись выше указанного алгоритма
    return list3

list1 = []
list2 = [3, 4, 5, 6]

if __name__ == '__main__':
    print(test1(list1, list2))