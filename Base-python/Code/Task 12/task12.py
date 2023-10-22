import sys

def check_spelling(dict_file_path, check_file_path):
    # Создаем пустой словарь
    dictionary = {}

    # Проверяем наличие файла словаря
    try:
        with open(dict_file_path, 'r') as file:
            # Читаем слова из файла и добавляем их в словарь
            for line in file:
                words = line.strip().split()
                for word in words:
                    dictionary[word.lower()] = 0
    except FileNotFoundError:
        print("Ошибка: Файл словаря не найден.")
        return

    # Открываем файл с текстом для проверки
    try:
        with open(check_file_path, 'r') as file:
            incorrect_words = []

            for line in file:
                words = line.strip().split()
                for word in words:
                    # Проверяем, содержится ли слово в словаре
                    if word.lower() not in dictionary:
                        incorrect_words.append(word)

            # Выводим список неправильно написанных слов
            if len(incorrect_words) > 0:
                print("Неправильно написанные слова:")
                for word in incorrect_words:
                    print(word)
            else:
                print("Ошибок в орфографии не найдено.")

    except FileNotFoundError:
        print("Ошибка: Файл для проверки не найден.")


# Проверяем наличие аргументов командной строки
if len(sys.argv) < 3:
    print("Ошибка: Необходимо указать два имени файла в аргументе командной строки.")
else:
    dict_file_path = sys.argv[1]
    check_file_path = sys.argv[2]
    check_spelling(dict_file_path, check_file_path)