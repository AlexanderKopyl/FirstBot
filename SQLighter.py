# -*- coding: utf-8 -*-
import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all_question(self):
        """ Получаем все вопросы """
        with self.connection:
            return self.cursor.execute('SELECT * FROM question').fetchall()

    def select_all_answer(self, question):
        """ Получаем все ответы к вопросам """
        with self.connection:
            return self.cursor.execute('SELECT * FROM answer WHERE question_id = ?', (question,)).fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM question WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM question').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
