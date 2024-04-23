import psycopg2


class DbClient:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        """Executes a given SQL query and returns all results."""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_all_table_names(self):
        query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public' AND table_type = 'BASE TABLE';
        """
        return [row[0] for row in self.execute_query(query)]

    def get_column_names_and_types(self, table_name):
        query = f"""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_name = '{table_name}' AND table_schema = 'public';
        """
        return self.execute_query(query)

    def close(self):
        self.cursor.close()
        self.connection.close()


# Usage example
# db = DbClient(dbname='your_database_name', user='your_username', password='your_password')
# tables = db.get_all_table_names()
# columns = db.get_column_names_and_types('employees')
# db.close()
