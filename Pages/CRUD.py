import streamlit as st
from class_DatabaseManager import DatabaseManager
from class_CRUD import CRUDOperations


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
    ["Create", "Read", "Update", "Delete", "Alter", "Insert"]
)


st.title(f"{operation} Operation")

if operation == "Create":
    st.subheader("Insert a Record")
    table_name = st.text_input("Table Name")
    num_fields = st.number_input("Number of Fields", min_value=1, step=1)
    fields = {}
    for i in range(int(num_fields)):
        col = st.text_input(f"Column {i + 1} Name")
        value = st.text_input(f"Column {i + 1} Value")
        if col:
            fields[col] = value
    if st.button("Submit"):
        try:
            crud_ops.create(table_name, fields)
            st.success("Record inserted successfully.")
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
    table_name = st.text_input("Table Name")
    num_fields = st.number_input("Number of Fields to Update", min_value=1, step=1)
    fields = {}
    for i in range(int(num_fields)):
        col = st.text_input(f"Field {i + 1} Name")
        value = st.text_input(f"Field {i + 1} New Value")
        if col:
            fields[col] = value
    condition = st.text_area("Condition")
    params = st.text_area("Condition Parameters (comma-separated)").split(",")
    if st.button("Submit"):
        try:
            crud_ops.update(table_name, fields, condition, params)
            st.success("Records updated successfully.")
        except Exception as e:
            st.error(f"Error: {e}")

elif operation == "Delete":
    st.subheader("Delete Records")
    table_name = st.text_input("Table Name")
    condition = st.text_area("Condition")
    params = st.text_area("Condition Parameters (comma-separated)").split(",")
    if st.button("Submit"):
        try:
            crud_ops.delete(table_name, condition, params)
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


st.sidebar.info("Thank you for using the application!")
if st.sidebar.button("Exit Application"):
    db_manager.close_connection()
    st.stop()
