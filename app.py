from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL connection details using host.docker.internal and specifying the port
db = mysql.connector.connect(
    host="181.215.246.169",  # Use host.docker.internal to access the host machine
    user="root",
    password="root",
    database="CCSD",
    port=3306  # Explicitly specifying the MySQL port
)

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM user WHERE userName = %s AND Password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
