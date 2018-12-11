from string import whitespace, punctuation
w_p = whitespace + punctuation

def enter_list():
    my_list = [" "]
    enter_string = "d"
    while enter_string != [""]:
        enter_string = (input("Введите строку:  ")).lower()
        if enter_string == "":
            print("Вы прервали программу!")
        for char in w_p:
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
    print("_____________________________________")
    print("Слова из текста отсортированные по алфавиту: \n")
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        else:
            print(word[i], end=" ")
    print(word[-1])

