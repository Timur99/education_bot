import requests
import json
import requests
from openai import OpenAI
from scriptss.config import load_credentials, DB_CREDENTIALS, TGRM_BOT_CREDENTIALS, OPENAI_API
from dotenv import load_dotenv
import os


# Загрузка переменных окружения
load_dotenv()


#creds = load_credentials(OPENAI_API)
#open_ai_key = creds['api_test']

open_ai_key = os.getenv('OPENAI') #, load_credentials(OPENAI_API)['api'])

client = OpenAI(api_key=open_ai_key)


def promt_context_json(system_prompt, user_promt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": str(system_prompt)},
                {"role": "user", "content": str(user_promt)}
            ],
            response_format={ "type": "json_object" }
        )
        return completion.choices[0].message.content
    except requests.exceptions.RequestException as e:
        return f"Ошибка при выполнении запроса: {e}"


def promt_context_string(system_prompt, user_promt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": str(system_prompt)},
                {"role": "user", "content": str(user_promt)}
            ]
        )
        return completion.choices[0].message.content
    except requests.exceptions.RequestException as e:
        return f"Ошибка при выполнении запроса: {e}"
