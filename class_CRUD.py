class CRUDOperations:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def create(self, table_name, schema):
        try:
            columns = ", ".join([f"{col} {datatype}" for col,datatype in schema.items()])  
            query = f"CREATE TABLE {table_name} ({columns})"
            self.db_manager.execute_query(query)
            print(f"Table '{table_name}' created successfully.")
        except Exception as e:
            print(f"Error during CREATE operation: {e}")

    
    def insert(self, table_name, data):
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.db_manager.execute_query(query, tuple(data.values()))
            print(f"Record inserted into {table_name}.")
        except Exception as e:
            print(f"Error during INSERT operation: {e}")

   
    def alter(self, table_name, operation, column_name=None, column_type=None):
        try:
            if operation == "add":
                query = f"ALTER TABLE {table_name} ADD {column_name} {column_type}"
            elif operation == "modify":
                query = f"ALTER TABLE {table_name} MODIFY {column_name} {column_type}"
            elif operation == "drop":
                query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
            else:
                raise ValueError("Invalid operation. Use 'add', 'modify', or 'drop'.")
            self.db_manager.execute_query(query)
            print(f"Table {table_name} altered successfully.")
        except Exception as e:
            print(f"Error during ALTER operation: {e}")

    
    def read(self, table_name, columns="*", condition=None, params=None):
        try:
            query = f"SELECT {columns} FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            return self.db_manager.fetch_data(query, params)
        except Exception as e:
            print(f"Error during READ operation: {e}")
            return []

    
    def update(self, table_name, data, condition, condition_params):
        try:
            set_clause = ", ".join([f"{col} = %s" for col in data.keys()])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"   
            query_params = tuple(data.values()) + tuple(condition_params)
            self.db_manager.execute_query(query, query_params)
            print(f"Records in table '{table_name}' updated successfully.")
        except Exception as e:
            print(f"Error during UPDATE operation: {e}")


    
    def delete(self, table_name, condition = None, params = None):
        try:
            if condition:
                query = f"DELETE FROM {table_name} WHERE {condition}"
            else:
                query = f"DELETE FROM {table_name}"
            self.db_manager.execute_query(query)
            print(f"Records deleted successfully from table '{table_name}'.")
        except Exception as e:
            print(f"Error during DELETE operation: {e}")

    
    def drop(self, table_name):
        try:
            query = f"DROP TABLE {table_name}"
            self.db_manager.execute_query(query)
            print(f"Table {table_name} as been Dropped Sucessfully!")
        except Exception as e:
            print(f"Error during DROP operation: {e}")
