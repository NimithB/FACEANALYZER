import mysql.connector

# MySQL Configuration
config = {
    'host': '127.0.0.1',
    'user': 'nimith',
    'password': '1234567890',
    'database': 'expression',  # Replace with your actual database name
    'port': 3306,
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci',
    'autocommit': True
}

# Function to create a table
def create_table():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Define the table creation SQL statement
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS analysis_results (
                name VARCHAR(255) NOT NULL,
                result_data TEXT,
                PRIMARY KEY (name)
            )
        '''

        # Execute the table creation SQL statement
        cursor.execute(create_table_query)
        print("Table 'analysis_results' created successfully")

        cursor.close()
        connection.close()

    except mysql.connector.Error as error:
        print(f"Error creating table: {error}")

# Create the table if it does not exist
if __name__ == '__main__':
    create_table()
