from .logger import logger
import ollama
import json


def llm_generate(prompt):
    response = ollama.generate(model="llama3", prompt=prompt, stream=False)
    return response["response"]


def llm_generate_json(prompt):
    response = ollama.generate(
        model="llama3", prompt=prompt, stream=False, format="json"
    )
    return json.loads(response["response"])


def llm_generate_embedding(prompt):
    response = ollama.embeddings(
        model="llama3",
        prompt=prompt,
    )

    return response["embedding"]


def generate_request_for_table_descriptions(db_context):
    return f"""
  Generate a JSON array with detailed descriptions for each table in the provided database context.
  Each entry in the array should be a plain string describing a table,
  including the table's name, and each column's name and type as specified in the database context.

  Database context: {db_context}

  The output should be a valid JSON array of plain strings. Each description should include:
  - Table name exactly as written in the database context,
  - Names and types of columns, with column names written exactly as they appear in the database context.

  Output structure should be {{ "tables": ['description one', 'description two', ...] }}

  Example below.
  Example database context:
  CREATE TABLE employee (
    id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    hire_date DATE
  );
  CREATE TABLE product (
    sku VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    stock INT
  );

  Example output:
  {{
    "tables": [
      "The employee table has four columns: id INT, first_name VARCHAR, last_name VARCHAR, hire_date DATE. The id column stores the unique identifier for each employee, the first_name column stores the employee's first name, the last_name column stores the employee's last name, and the hire_date column records the date when the employee was hired.",
      "The product table has four columns: sku VARCHAR, description TEXT, price DECIMAL, stock INT. The sku column stores the stock keeping unit for each product, the description column provides a text description of the product, the price column records the product's price as a decimal value, and the stock column counts the quantity of the product available in inventory."
    ]
  }}
  """


def generate_table_descriptions(db_context):
    logger.info("Generating table descriptions...")

    request = generate_request_for_table_descriptions(db_context)
    response = llm_generate_json(request)
    table_descriptions = response["tables"]

    logger.info(f"Table descriptions generated.\n{table_descriptions}")

    return table_descriptions
