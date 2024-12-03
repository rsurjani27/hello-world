import os
import subprocess
import mysql.connector
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials (sensitive data exposure)
DB_USER = "admin"
DB_PASS = "super_secret_password"

@app.route('/')
def index():
    # SQL Injection vulnerability
    user_id = request.args.get('user_id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    
    connection = mysql.connector.connect(user=DB_USER, password=DB_PASS, database='example_db')
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    # Cross-Site Scripting (XSS) vulnerability
    return render_template_string(f"<h1>User Details: {result}</h1>")

@app.route('/run_command')
def run_command():
    # Command Injection vulnerability
    cmd = request.args.get('cmd')
    output = subprocess.check_output(cmd, shell=True)
    return output

@app.route('/read_file')
def read_file():
    # Path Traversal vulnerability
    filename = request.args.get('filename')
    with open(filename, 'r') as file:
        content = file.read()
    return content

@app.route('/eval_code')
def eval_code():
    # Code Injection vulnerability
    code = request.args.get('code')
    return str(eval(code))

if __name__ == '__main__':
    # Insecure configuration
    app.run(debug=True, host='0.0.0.0', port=5000)
