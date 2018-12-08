from string import punctuation, whitespace


def enter_list():
    my_list = [" "]
    enter_string = "d"
    while enter_string != [""]:
        enter_string = (input("Введите строку:  ")).lower()
        if enter_string == "":
            print("Вы прервали программу!")
        for char in punctuation or whitespace:
            enter_string = enter_string.replace(char, " ")
        enter_string = enter_string.split(" ")
        my_list = my_list + enter_string
    return my_list


word = enter_list()
word.sort()
while word[0] == "":
    word.remove("")
word.remove(" ")
long_word = len(word)
if long_word < 1:
    print("Вы не ввели слов для статистики!")
if long_word != 0:
    print("Введенные слова для обработки:  ", word, "\n")
    print("Статистика слов: \n")
    print("| {:^30}  | {:^30} |".format("СЛОВО", "КОЛЛИЧЕСТВО ПОВТОРЕНИЙ"))
    print("|_________________________________|________________________________|")
    rez = 1
    for i in range(0, long_word - 1):
        if word[i] == word[i + 1]:
            rez += 1
            continue
        if word[i] != word[i + 1]:
            print("| {:<30}  | {:>30} |".format(word[i], rez))
            rez = 1
    if long_word < 2:
        print("| {:<30}  | {:>30} |".format(word[0], 1))
    elif word[-1] != word[-2]:
        print("| {:<30}  | {:>30} |".format(word[-1], 1))
    elif word[-1] == word[-2]:
        print("| {:<30}  | {:>30} |".format(word[-1], rez))

