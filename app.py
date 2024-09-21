from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection details
db = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="your_db"
)

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
