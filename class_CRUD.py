class CRUDOperations:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def create(self, table_name, data):
        try:
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.db_manager.execute_query(query, tuple(data.values()))
            print(f"Record inserted successfully into {table_name}.")
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

    
    def update(self, table_name, data, condition, params):
        try:
            set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
            self.db_manager.execute_query(query, tuple(data.values()) + tuple(params))
            print(f"Records in {table_name} updated successfully.")
        except Exception as e:
            print(f"Error during UPDATE operation: {e}")

    
    def delete(self, table_name, condition, params):
        try:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            self.db_manager.execute_query(query, params)
            print(f"Records deleted from {table_name}.")
        except Exception as e:
            print(f"Error during DELETE operation: {e}")
