# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Удаляем запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = 6")

# общее количество записей
cursor.execute("SELECT COUNT(*) FROM Users")
all_records = cursor.fetchone()[0]
print(all_records)

# сумма всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print(sum_balance)

# средний баланс пользователей
print(f'Средний баланс пользователей: {sum_balance/all_records}')



connection.commit() # сохраняем состояние
connection.close() # закрываем соединение