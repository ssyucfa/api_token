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
                                         database="words_all")
        try:
            cur = myconn.cursor()
            cur.execute(f"select question from words_{language}")
            result = cur.fetchall()
            question = []
            for i in result:
                question.append(i[0])

            question = random.choice(difflib.get_close_matches(message, question))

            response = []

            cur.execute(
                f"select response from words_{language} where question like '{question}%'")
            result = cur.fetchall()
            for i in result:
                response.append(i[0])

            word = random.choice(response)

            return word
        except Exception as exception:
            myconn.close()

            return f'{exception=}'
    except Exception as error:
        return f'{error=}'

