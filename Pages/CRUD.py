import streamlit as st
from class_DatabaseManager import DatabaseManager
from class_CRUD import CRUDOperations
import pandas as pd


try:
    db_manager = DatabaseManager(
        user="gokulgowtham",
        password="Iamgokul@123",
        host="localhost",
        database="new_tab"
    )
    st.success("Database connection established successfully.")
except Exception as e:
    st.error(f"Failed to connect to the database: {e}")
    st.stop()

crud_ops = CRUDOperations(db_manager)


st.sidebar.title("CRUD OPERATIONS")
operation = st.sidebar.selectbox(
    "Select Operation",
    ["Create", "Read", "Update", "Delete", "Alter", "Insert","Drop"]
)


st.title(f"{operation} Operation")

if operation == "Create":
    st.subheader("Create a Table")
    table_name = st.text_input("Table Name")
    num_fields = st.number_input("Number of Fields", min_value=1, step=1)
    fields = {}
    for i in range(int(num_fields)):
        col = st.text_input(f"Column {i + 1} Name")
        value = st.text_input(f"Column {i + 1} Datatype (e.g., TEXT, INTEGER, etc.)")
        if col and value:
            fields[col] = value
    if st.button("Submit"):
        try:
            crud_ops.create(table_name, fields)
            st.success(f"Table '{table_name}' created successfully.")
        except Exception as e:
            st.error(f"Error: {e}")


elif operation == "Read":
    st.subheader("Read Records")
    table_name = st.text_input("Table Name")
    condition = st.text_area("Condition (Optional)")
    if st.button("Fetch Records"):
        try:
            data = crud_ops.read(table_name, condition=condition or None)
            if data:
                st.dataframe(data)
            else:
                st.info("No records found.")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Update":
    st.subheader("Update Records")
    try:
        cursor = db_manager.connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
        table_name = st.selectbox("Select Table", tables)
        
        if table_name:
            cursor.execute(f"DESCRIBE {table_name}")
            columns = [column[0] for column in cursor.fetchall()]
            cursor.execute(f"SELECT * FROM {table_name}")
            current_data = cursor.fetchall()
            st.write("Current Data:")
            df = pd.DataFrame(current_data, columns=columns)
            st.dataframe(df)
            with st.form("update_form"):
                where_column = st.selectbox("Select WHERE Column", columns)
                where_value = st.text_input("Enter WHERE Value")
                st.write("Select fields to update:")
                update_fields = {}
                
                for col in columns:
                    if st.checkbox(f"Update {col}"):
                        new_value = st.text_input(f"New value for {col}")
                        if new_value:
                            update_fields[col] = new_value
                submitted = st.form_submit_button("Update Record")
                
                if submitted and where_value and update_fields:
                    try:
                        condition = f"{where_column} = %s"
                        condition_params = [where_value]
                        crud_ops.update(table_name, update_fields, condition, condition_params)
                        st.success("Records updated successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
    
    except Exception as e:
        st.error(f"Error connecting to database: {e}")


elif operation == "Delete":
    st.subheader("Delete Records")
    table_name = st.text_input("Table Name")
    condition = st.text_area("Condition")
    if st.button("Submit"):
        try:
            if condition: 
                crud_ops.delete(table_name, condition)
            else:  
                crud_ops.delete(table_name)
            st.success("Records deleted successfully.")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Alter":
    st.subheader("Alter Table")
    table_name = st.text_input("Table Name")
    operation_type = st.selectbox("Operation Type", ["Add", "Modify", "Drop"])
    column_name = st.text_input("Column Name")
    column_type = None
    if operation_type in ["Add", "Modify"]:
        column_type = st.text_input("Column Data Type")
    if st.button("Submit"):
        try:
            crud_ops.alter(table_name, operation_type.lower(), column_name, column_type)
            st.success(f"Table {operation_type} operation successful.")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Insert":
    st.subheader("Insert Records")
    table_name = st.text_input("Table Name")
    num_fields = st.number_input("Number of Fields", min_value=1, step=1)
    fields = {}
    for i in range(int(num_fields)):
        col = st.text_input(f"Field {i + 1} Name")
        value = st.text_input(f"Field {i + 1} Value")
        if col:
            fields[col] = value
    if st.button("Submit"):
        try:
            crud_ops.insert(table_name, fields)
            st.success("Record inserted successfully.")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == 'Drop':
    st.subheader("Drop Table")
    table_name = st.text_input("Table Name")
    if st.button("Submit"):
        try: 
            crud_ops.drop(table_name)
            st.success("Table Dropped successfully.")
        except Exception as e:
            st.error(f"Error: {e}")


st.sidebar.info("Thank you for using the application!")
if st.sidebar.button("Exit Application"):
    db_manager.close_connection()
    st.stop()
