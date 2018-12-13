from string import whitespace, punctuation

n = 0


def get_vocabluary(text):  # функция преобразовывает текст в словарь переводов слов текста
    def translate(word):  # функция получает перевод слова
        enter_string = ""
        pun = '"""!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
        whit = '\t\n\r\x0b\x0c'
        w_p = whit + pun
        while enter_string == "":
            print('Слово "', word, '" не известною')
            # переводим введёный текст в нижний регистр
            enter_string = (input("Введите перевод слова на английский или русский язык:  ")).lower()
            enter_string.lower()
            for char in w_p:  # проверяем правильность ввода текста на наличие служебных символов
                if char in enter_string:
                    enter_string = ""
        return enter_string

    def text_change(text):  # функция обрабатывает текст и возвращает список слов
        text = text.lower()
        for char in whitespace:  # очищаем текст от служебных символов ' \t\n\r\x0b\x0c'
            if char in text:
                text = text.replace(char, " ")
        for char in punctuation:  # очищаем текст от служебных символов '"""!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
            if char in text:
                text = text.replace(char, " ")
        text = text.split(" ")  # разделяем текст по пробелам
        text.sort()  # сортируем текст по алфавиту
        while text[0] == "":  # убараем все пробелы
            text.remove("")
        return text

    fist_text = text_change(text)

    def get_vocab(fist_text):  # функция создает словарь преводов
        for i in range(0, len(fist_text)):  # преобразовываем список слов из текста в словарь
            result = dict((i, None) for i in fist_text)
        for i in range(0, len(fist_text)):  # определяем знакомо на слово или нет
            if result.get(fist_text[i]) is None:  # если слово не знакомо - запускаем функцию перевода слова
                result[fist_text[i]] = translate(fist_text[i])
        return result

    fist_dict = get_vocab(fist_text)
    new_text = ""
    # запрашиваем новый текст или выход из программы
    while new_text == "":
        new_text = input("Введите новый текст или exit для выхода из программы: ")
        for char in punctuation:
            if char in new_text or char == "":
                new_text = ""
        if new_text == "":
            continue
        elif new_text != "exit":
            new_list = text_change(new_text)
            for i in range(0, len(new_list)):  # создаем новый словарь переводов
                if new_list[i] not in fist_dict:  # проверяем знакомо ли нам слово
                    fist_dict[new_list[i]] = translate(new_list[i])  # если слово не знакомо переводим его
            new_text = ""
    return fist_dict


if __name__ == "__main__":
    vocabluary = {}
    text = """Здесь определяется текст на котором будет продемонстрирована правильность работы программы.
    Текст должен быть многострочным.

    В тексте должны быть пустые строки
    и использоваться знаки из whitespace, например """ + "\t" + """табуляция"""
    while text != "" and n == 0:
        vocabluary.update(get_vocabluary(text))  # переводим исходный текст
        print("\n")
        print("| {:^30}  | {:^30} |\n".format("СЛОВО", "ПЕРЕВОД"))  # отображаем словарь переводов
        for key, value in vocabluary.items():
            print("|  {:<30} | {:^30} |".format(key, value))
        n = 1
