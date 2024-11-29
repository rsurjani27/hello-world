# this file is used for testing purpose in my personal github account
import os
import subprocess

def insecure_function(user_input):
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    
    # Command Injection vulnerability
    os.system(f"echo {user_input}")
    
    # Arbitrary code execution
    eval(user_input)
    
    # Insecure use of subprocess
    subprocess.call(user_input, shell=True)

# Hardcoded credentials
PASSWORD = "super_secret_password"

# Insecure random number generation
import random
secret_key = random.randint(1, 100)
