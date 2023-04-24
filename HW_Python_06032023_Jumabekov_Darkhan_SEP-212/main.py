'''
5*) Дмитрий считает, что когда текст пишут в скобках (как вот тут, например),
его читать не нужно. Вот и надумал он существенно укоротить время чтения,
написав функцию, которая будет удалять все, что расположено внутри скобок.
'''
import string
import re

def shortener(text):
    return re.sub(r'\s?\([^)]+\)*(\))*', '', text).strip()

'''
1) Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
в котором каждый элемент списка является и ключом и значением. 
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
'''

def to_dict(lst):
    my_dict = {}
    for elem in lst:
        my_dict[elem] = elem
    return my_dict.items()

'''
6*) Александр решил как-то отобразить в тексте BACKSPACE (т.е. удаление последнего символа). 
Он подумал, что символ @ отлично для этого подходит. 
Всем своим знакомым он дал строки такого вида (например, гр@оо@лк@оц@ва), 
чтобы посмотреть, кому удастся написать функцию cleaned_str(st), возвращающую строку в ее чистом виде.
'''
def cleaned_str(st):
    result_lst = []
    for elem in st:
        if elem == '@' and len(st) > 0:
            result_lst.pop()
        else:
            result_lst.append(elem)
    return ''.join(result_lst)

'''
6*) На входе имеем список строк разной длины. Необходимо написать функцию all_eq(lst), 
которая вернет новый список из строк одинаковой длины.
Длину итоговой строки определяем исходя из самой большой из них. 
Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями 
с правого края до требуемого количества символов.
Расположение элементов начального списка не менять.
'''

def all_eq(lst: list):
    new_lst = []
    max_len_elem = 0
    for elem in lst:
        if len(elem) > max_len_elem:
            max_len_elem = len(elem)
    for elem in lst:
        if len(elem) <= max_len_elem:
            temp = ''
            for i in range(max_len_elem - len(elem)):
                temp += '_'
            new_lst.append(elem+temp)
    return new_lst


'''
5*) Предоставлен список натуральных чисел. 
Требуется сформировать из них множество. Если какое-либо число повторяется, то преобразовать его в строку по образцу: 
например, если число 4 повторяется 3 раза, то в множестве будет следующая запись: 
само число 4, строка 44 (второе повторение, т.е. число дублируется в строке), 
строка 444 (третье повторение, т.е. строка множится на 3). Реализуйте вывод множества через функцию set_gen().
'''

def set_gen(lst):
    my_set = set()
    for elem in lst:
        count = lst.count(elem)
        my_set.add(elem)
        for i in range(1, count):
            my_set.add(str(elem) * (i+1))
    return my_set


if __name__ == '__main__':
    # Task 1
    text = 'Дмитрий считает, что когда текст пишут в скобках (как вот тут, например (или тут)), его читать не нужно. Помогите ленивому Диме разработать функцию shortener(st)'
    print(shortener(text))
    # Task 2
    lst = ['hello', 'world', 'привет', 'мир']
    print(to_dict(lst))
    # Task 3
    text = 'гр@оо@лк@оц@ва'
    print(cleaned_str(text))
    #Task 4
    lst = ['aaaa', 'bbbbbb', 'ccc', 'dddddddd']
    print(all_eq(lst))
    #Task 5
    lst = [1, 4, 3, 4, 3, 2, 1, 4]
    print(set_gen(lst))