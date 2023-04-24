'''
Задание №1
Дан текстовый файл. Необходимо создать новый файл убрав из него все неприемлемые
слова. Список неприемлемых слов находится в другом файле.
'''

def create_filtered_file(filename, fw):
    with open(filename, "w", encoding='utf-8') as file1:
        file1.write("красный оранжевый синий \n желтый черный зеленый \n белый голубой фиолетовый")
        file1.close()

    with open(filename, "rt", encoding='utf-8') as file1:
        if file1 is not None:
            file2 = open('file2.txt', mode='w', encoding='utf-8')
            for line in file1:
                words = line.split(' ')
                for w in words:
                    if not fw.__contains__(w):
                        file2.writelines([w, ' '])

'''
Задание №2
Написать программу транслитерации с русского на английский и наоборот. Данные для
транслитерации берутся из файла и записываются в другой файл. Направление перевода
определяется через меню пользователя
'''

def transliterate(text, lang='rus'):
    filename = 'rus_eng.txt' if lang == 'rus' else 'eng_rus.txt'

    with open(filename, "rt", encoding='utf-8') as rus_eng_file:
        if rus_eng_file is not None:
            rus_eng_dict = {}
            for line in rus_eng_file:
                rus_eng = line.replace('\n', '')
                letters = rus_eng.split(':')
                rus_eng_dict[letters[0]] = letters[1]
    result_text = text.lower()
    for letter in result_text:
        if letter.isalpha():
            result_text = result_text.replace(letter, rus_eng_dict[letter])
        else:
            result_text = result_text.replace(letter, letter)
    return result_text

'''
Задание №3
Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово
quit. После завершения ввода программа должна объединить содержимое всех перечисленных
пользователем файлов в один.
'''

def combine_files():
    files = []
    while True:
        filename = input('Введите название файла: ')
        if filename == 'quit': break
        filename = filename if filename.endswith('.txt') else filename + '.txt'
        files.append(filename)

    file_result = open('combine_files.txt', mode='w', encoding='utf-8')
    for f in files:
        file = open(f, "rt", encoding='utf-8')
        for line in file:
            file_result.writelines([line, ' '])

'''
Задание №4
Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово
quit. После завершения ввода программа должна записать в итоговый файл символы, которые
есть во всех перечисленных файлах (символы должны быть в каждом файле).
'''


def combine_symbols_from_files():
    files = []
    texts = []
    s = set()
    while True:
        filename = input('Введите название файла: ')
        if filename == 'quit':
            break
        filename = filename if filename.endswith('.txt') else filename + '.txt'
        files.append(filename)

    for file in files:
        with open(file,  mode='r', encoding='utf-8') as file:
            texts.append(set(file.read()))
    s = set(texts[0])
    for i in range(1, len(texts)):
        s = s.intersection(texts[i])
    file_result = open('combine_symbols_from_files.txt', mode='w', encoding='utf-8')
    file_result.writelines([s.__str__(), ' '])


if __name__ == '__main__':
    # Task 1
    forbidden_words = ['синий', 'черный', 'белый']
    # create_filtered_file('file1.txt', forbidden_words)

    # Task 2
    text_rus = "Написать программу транслитерации с русского на английский и наоборот"
    text_eng = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

    # print(transliterate(text_rus, 'rus'))
    # print(transliterate(text_eng, 'eng'))

    # Task 3
    # combine_files()

    # Task 4
    combine_symbols_from_files()
