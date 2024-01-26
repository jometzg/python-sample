# samnple flask app. One route to return a name from the environment variables
# and another route to return the body of a POST request as JSON, delegated to
# a second remote API endpoint.

import os
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv

app = Flask(__name__) 

# Load environment variables from .env file
load_dotenv()

# home route
@app.route('/') 
def home(): 
  return "Hello, World!" 

@app.route('/api/data', methods=['GET']) 
def get_data(): 
  # fetch a Name from the environment 
  data = {"key": os.getenv("NAME")} 
  return jsonify(data) 

@app.route('/api/data', methods=['POST']) 
def post_data(): 
  # return what was sent body as JSON 
  data = request.get_json() 
  return jsonify(data), 201 

@app.route('/api/todo', methods=['POST']) 
def post_todo(): 
    # get the body of the request 
    data = request.get_json() 

    # Make an HTTP POST request to the "URL" endpoint
    response = requests.post(os.getenv("URL"), json=data)

    # Return the response as JSON with status code 201
    return jsonify(response.json()), 201 


if __name__ == '__main__': 
  app.run(debug=True) 
