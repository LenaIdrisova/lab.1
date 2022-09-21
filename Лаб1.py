import csv
import random

with open('books.csv', 'r', encoding='windows-1251') as csvfile: #открытие файла с записями книг
    table = csv.reader(csvfile, delimiter=';') #считывание таблицы
    result = open('result.txt', 'w') #запись ссылок
    cz = 0
    cz30 = 0
    author = input('Имя автора: ')
    books = []
    links = []
    print(author)
    i = random.randint(1, 9391)
    for idx, row in enumerate(list(table)[1:]):
        if i <= idx <= i + 20:
            link = row[3] + '. ' + row[1] + ' - ' + row[6][:4]
            result.write(link + '\n')
            # result.write('\n') #перенос на новую строку
        if len(row[1]) > 30:
            cz30 += 1
        if row[3] == author or row[4] == author:
            books.append(row) #добавить новую запись в массив
        cz += 1
    print(cz, '-количество записей')
    print(cz30, '-количество записей, у которых в поле Название строка длиннее 30 символов')
    print('Книги автора ', author, ': ', books )

result.close()
