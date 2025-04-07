from flask import Flask, jsonify
import mysql.connector
from api.config.db_config import DB_CONFIG  
import sys
import os

# Add project root (nifty50_analysis/) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.db_config import DB_CONFIG  # ✅ Now it should work
app = Flask(__name__)

@app.route('/get_live_data')
def get_live_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM real_time_stock_data ORDER BY timestamp DESC LIMIT 50")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    