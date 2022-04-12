from typing import Union, Type

from django.core.cache import cache

import difflib
import random
import mysql.connector
from mysql.connector import MySQLConnection


def trap_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            return 'error'
    return wrapper


class WordsAccessor:
    def __init__(self) -> None:
        self.db: MySQLConnection = mysql.connector.connect(
            host='localhost',
            user='user_root',
            password='123Df321!',
            database="word_all"
        )

    @trap_error
    def _get_questions(self, language: str, cursor) -> list[str]:
        cursor.execute(f"select question from words_{language}")

        results = cursor.fetchall()

        questions = [i[0] for i in results]
        return questions

    @trap_error
    def _get_answer(self, question, language: str, cursor):
        cursor.execute(
            f"select response from words_{language} where question like '{question}%'"
        )

        results = cursor.fetchall()

        response = [i[0] for i in results]
        answer = random.choice(response)
        return answer

    @staticmethod
    def _get_queryset_from_cache(language: str) -> Union[list[str], bool]:
        return cache.get(f'questions_{language}', False)

    @staticmethod
    def _get_question(text: str, questions: list[str]):
        return random.choice(difflib.get_close_matches(text, questions))

    @trap_error
    def get_answer(self, get_message: str):
        language = get_message[0:2]
        text = get_message[2:-18]
        message_id = get_message[-18:]
        
        cursor = self.db.cursor()

        queryset = self._get_queryset_from_cache(language)
        if not queryset:
            questions = self._get_questions(language, cursor)

            cache.set(f'questions_{language}', questions, None)
            queryset = questions

        question = self._get_question(text, queryset)
        answer = self._get_answer(question, language, cursor)
        return answer


def do_magic(message: str) -> str:
    words = WordsAccessor()
    return words.get_answer(message)

words = WordsAccessor()
