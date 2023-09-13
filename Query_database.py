import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute an SQL query
query = "SELECT * FROM my_table"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Process and print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
