# app.py 
import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

app = Flask(__name__) 

# app.py
# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Rest of your code...

@app.route('/') 
def home(): 
  return "Hello, World!" 

@app.route('/api/data', methods=['GET']) 
def get_data(): 
  # Replace with your data fetching logic 
  data = {"key": os.getenv("NAME")} 
  return jsonify(data) 

@app.route('/api/data', methods=['POST']) 
def post_data(): 
  # Replace with your data processing logic 
  data = request.get_json() 
  return jsonify(data), 201 

if __name__ == '__main__': 
  app.run(debug=True) 

 
