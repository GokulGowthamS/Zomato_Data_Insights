# Project Overview  

The Zomato Data Insights Application provides an interactive interface for performing CRUD operations (Create, Read, Update, Delete) on a MySQL database related to Zomato data.The application uses Streamlit for the web interface, and the core functionality is handled through a **DatabaseManager** class for database interactions and a **CRUDOperations** class for handling SQL operations.The main objective of this project is to provide an easy-to-use platform for database manipulation, allowing users to interact with the Zomato data efficiently and effectively.

# Pages  

This Folder contains files used for the front end of the Streamlit application.   

- CRUD.py  
- Query.py  
- Table.py  

### CRUD.py  
This Python file is used for CRUD operations for the application by connecting to the MYSQL Database.   

**Create**: Add new records to a table.  
**Read**: Retrieve and display records with optional filters.  
**Update**: Modify records based on conditions.  
**Delete**: Remove records using specified criteria.  
**Alter**: Add, modify, or drop table columns.  
**Insert**: Insert records into existing tables.  

- The database connection is managed via **DatabaseManager**, and **CRUDOperations** handles the operations.  
- Errors are caught and displayed to ensure usability.  
- It includes an option to close the database connection and exit the app.

### Query.py  
This Python file has all 20 queries structured to show the result data by connecting to a MySQL database and provides a dropdown menu to execute predefined SQL queries.  

**Database Connection**: Connects to new_tab database using MySQL.  
**Query Selection**: Users choose from 21 queries, each targeting specific insights (e.g., peak ordering locations, customer segmentation, average delivery time).  
**Query Execution**: The selected query is executed using cursor.execute(), and results are fetched using Pandas for display in a DataFrame.  
**Interactive UI**: Displays query results in an interactive table within the app.  

Each query is mapped to an operation, focusing on customer trends, delivery metrics, and order patterns.  

### Table.py  

This Python file allows users to view datasets interactively by selecting from predefined table options.  

**Title**: Displays the title "Table View."  
**Table Selection**: Users can choose between "Customers," "Restaurants," "Orders," and "Deliveries."  
**Data Display**: The corresponding CSV file is loaded and displayed in a scrollable, interactive table format based on the selection.  

Each table corresponds to a dataset stored locally, providing a convenient way to explore Zomato data insights.  

# Scripts  

This Folder has all the data that is used for Database connectivity and Data Generation.  

### Data Sets.py  

- This Python script generates synthetic data for a Zomato-like business scenario using the Faker library and randomization.  
- It creates datasets for **customers**, **restaurants**, **orders**, and **deliveries**, with each dataset containing 10 records.  
- The generated data includes attributes like customer details, restaurant information, order specifics, and delivery details.  
- Finally, the script saves each dataset into separate CSV files for further use.  

### SQLconnection.py  

- This Python script connects to a MySQL database and creates tables for managing a business dataset, including __Customers__, __Restaurants__, __Orders__, and __Deliveries__.  
- It defines the schema for each table and sets up relationships through foreign keys.  
- The script reads data from respective CSV files, processes them, and inserts the data into the created tables using SQL **INSERT** statements.  
- After completing the data insertion, it closes all database connections.   
- Finally, it prints confirmation messages for the successful creation of tables and data insertion.  

# class_CRUD.py  

- The **CRUDOperations** class provides a structured approach to managing database operations.  
- It leverages a db_manager object to execute queries and includes methods for the following operations,

          Create: Inserts a new record into a specified table using key-value pairs for column names and values.
          Insert: Similar to the create method, it adds records to a table with specified data.
          Alter: Modifies a table by adding, modifying, or dropping columns based on the operation type.
          Read: Retrieves data from a specified table with optional filtering conditions.
          Update: Updates records in a table based on specified data and conditions.
          Delete: Removes records from a table based on given conditions.
  
- Each method handles exceptions and provides feedback on success or failure.

# class_DataManager.py  

- The **DatabaseManager** class manages MySQL database connections and queries. It includes methods for,  

          Connection: Establishes a connection to the database, retrying a specified number of times in case of failure.
          fetch_tables: Retrieves a list of all tables in the connected database.
          fetch_columns: Fetches the columns of a specified table.
          execute_query: Executes a SQL query with optional parameters, committing changes to the database.
          fetch_data: Retrieves data from the database based on a query.
          fetch_data_as_dataframe: Fetches data as a pandas DataFrame.
          close_connection: Closes the cursor and database connection.
          Context Manager: Implements context management methods (__enter__ and __exit__) for automatic connection handling.
  
- Each method handles exceptions and ensures proper connection management.

# main.py  

This python file just provides the front page of the whole application.






