import mysql.connector as db
import pandas as pd
import time

class DatabaseManager:
    def __init__(self, user, password, database, host="localhost", retries=3):
        for attempt in range(retries):
            try:
                self.connection = db.connect(
                    user=user,
                    password=password,
                    host=host,
                    database=database
                )
                self.cursor = self.connection.cursor()
                print("Database connection established successfully.")
                break
            except db.Error as e:
                print(f"Error connecting to the database: {e}. Retrying {attempt + 1}/{retries}...")
                time.sleep(2)
                if attempt == retries - 1:
                    raise

    def fetch_tables(self):
        try:
            self.cursor.execute("SHOW TABLES")
            return [table[0] for table in self.cursor.fetchall()]
        except db.Error as e:
            print(f"Error fetching tables: {e}")
            return []

    def fetch_columns(self, table_name):
        try:
            self.cursor.execute(f"DESCRIBE {table_name}")
            return [row[0] for row in self.cursor.fetchall()]
        except db.Error as e:
            print(f"Error fetching columns for table {table_name}: {e}")
            return []

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except db.Error as e:
            error_message = f"Error executing query: {query}\nParams: {params}\nError: {e}"
            print(error_message)
            self.connection.rollback()
            raise db.Error(error_message)

    def fetch_data(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except db.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_data_as_dataframe(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            data = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]
            return pd.DataFrame(data, columns=columns)
        except db.Error as e:
            print(f"Error fetching data as DataFrame: {e}")
            return pd.DataFrame()

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Database connection closed.")
        except db.Error as e:
            print(f"Error closing the database connection: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_connection()
