from scriptss.llm_script import get_tasks

objects = input('Введи предмет, по которому хочешь полуить задачу: ' )
rang = input('Какой уровень сложности: ' )

get_tasks(objects, rang)