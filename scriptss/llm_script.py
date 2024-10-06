import json
import requests
from openai import OpenAI
from scriptss.config import load_credentials, DB_CREDENTIALS, TGRM_BOT_CREDENTIALS, OPENAI_API
import os
from wrappers.requests_llm import promt_context_string


def get_tasks(objects, rang):
    system_prompt = f'''
        Ты крутой репетитор, тебе нужно придумать задачу для ученика.
        На вход подается название предмета и его сложность
        
        В ответе должно быть 4 варианта ответа и обьяснение правильного
        
        Формат ответа
        Задача:
        Варианты ответа:
        Ответ:
    '''

    user_promt = f'''
            Тема задачи: {objects}
            Сложность задачи: {rang}
        '''

    t = promt_context_string(system_prompt, user_promt)
    print(t)

    return t



if __name__ == '__main__':
    creds = (load_credentials(OPENAI_API))
    print(creds['api_test'])
    #print(load_credentials(TGRM_BOT_CREDENTIALS))
    #print(load_credentials(DB_CREDENTIALS))

    objects = 'python' #input('Введи предмет, по которому хочешь полуить задачу: ' )
    rang = 'easy' #input('Какой уровень сложности: ' )

    get_tasks(objects, rang)