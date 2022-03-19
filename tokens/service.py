from django.core.cache import cache

import difflib
import random
import mysql.connector


def magic(get_message):
    try:
        language = get_message[0:2]
        message = get_message[2:]
        myconn = mysql.connector.connect(host='localhost',
                                         user='user_root',
                                         password='123Df321!',
                                         database="word_all")
        try:
            cur = myconn.cursor()
            qs = cache.get(f'questions_{language}', False)
            if not qs:
                cur.execute(f"select question from words_{language}")
                result = cur.fetchall()
                questions = []
                for i in result:
                    questions.append(i[0])

                cache.set(f'questions_{language}', questions, None)
                qs = questions

            question = random.choice(difflib.get_close_matches(message, qs))

            response = []

            cur.execute(
                f"select response from words_{language} where question like '{question}%'")
            result = cur.fetchall()
            for i in result:
                response.append(i[0])

            word = random.choice(response)

            return word
        except Exception as _:
            myconn.close()

            return 'error'
    except Exception as _:
        return 'error'
