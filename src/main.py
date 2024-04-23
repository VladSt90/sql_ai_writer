from utils.db_utils import DbClient

DB_NAME = "dvdrental"
DB_USER = "test"
DB_PASSWORD = "test"

client = DbClient(
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

print(client.get_column_names_and_types("actor"))


# import ollama

# response = ollama.generate(model='llama3', prompt='why is the sky blue?', stream=False)
# print(response['response'])
