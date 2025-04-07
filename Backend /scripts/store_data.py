import mysql.connector
from config.db_config import DB_CONFIG  # Import database config

def save_to_db(symbol, price):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO real_time_stock_data (symbol, price, timestamp) VALUES (%s, %s, NOW())"
        cursor.execute(query, (symbol, price))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
