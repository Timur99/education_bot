import json
import requests
from openai import OpenAI
from scriptss.config import load_credentials, DB_CREDENTIALS, TGRM_BOT_CREDENTIALS, OPENAI_API
from dotenv import load_dotenv
import os


# Загрузка переменных окружения
load_dotenv()


def process_text(prompt):
    #creds = load_credentials(OPENAI_API)
    #open_ai_key = os.getenv('OPENAI')  #creds['api']

    open_ai_key = os.getenv('OPENAI') #, load_credentials(OPENAI_API)['api'])

    client = OpenAI(api_key=open_ai_key)

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except requests.exceptions.RequestException as e:
        return f"Ошибка при выполнении запроса: {e}"

def promt_context(promt):

    response = process_text(promt)
    return response


def get_tasks(objects, rang):
    promt = f'''
        Придумай задачу с 4 вариантами ответа по {objects}
        Сложность задачи {rang}
        
        Формат ответа
        Задача:
        Варианты ответа:
        Ответ:
    '''

    t = promt_context(promt)
    print(t)

    return t



if __name__ == '__main__':
    creds = (load_credentials(OPENAI_API))
    print(creds['api'])
    print(load_credentials(TGRM_BOT_CREDENTIALS))
    print(load_credentials(DB_CREDENTIALS))

    objects = input('Введи предмет, по которому хочешь полуить задачу: ' )
    rang = input('Какой уровень сложности: ' )

    get_tasks(objects, rang)