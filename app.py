import os
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv

app = Flask(__name__) 

# Load environment variables from .env file
load_dotenv()

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

@app.route('/api/todo', methods=['POST']) 
def post_todo(): 
    # Replace with your data processing logic 
    data = request.get_json() 

    # Make an HTTP POST request to the desired endpoint
    response = requests.post(os.getenv("URL"), json=data)

    # Return the response as JSON with status code 201
    return jsonify(response.json()), 201 


if __name__ == '__main__': 
  app.run(debug=True) 
