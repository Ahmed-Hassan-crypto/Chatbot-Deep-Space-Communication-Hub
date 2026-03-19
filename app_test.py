import sqlite3

ADMIN_PASSWORD = "AdminPassword123!" 
API_KEY = "sk-12345-abcde-98765-qwerty"

def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = " + user_id
    
    print(f"Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchone()

def login(input_password):
    if input_password == ADMIN_PASSWORD:
        return "Welcome Admin!"
    else:
        return "Login failed. The password you entered is incorrect for the 'admin' account."

user_input = "1 OR 1=1" 
print(get_user_data(user_input))
