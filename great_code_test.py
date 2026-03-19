import sqlite3
import os
import bcrypt  
from dotenv import load_dotenv 

load_dotenv()

ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH")
DB_PATH = os.getenv("DATABASE_URL", "users.db")

def get_user_data(user_id: int):
    """
    Fetches user data using secure parameterized queries.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
          
            query = "SELECT id, username, email FROM users WHERE id = ?"
            
            cursor.execute(query, (user_id,))
            return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return None

def verify_login(input_password: str):
    if bcrypt.checkpw(input_password.encode(), ADMIN_PASSWORD_HASH.encode()):
        return {"status": "success", "message": "Welcome back!"}

    return {"status": "error", "message": "Invalid credentials."}

if __name__ == "__main__":
    print(get_user_data(1))
