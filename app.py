from flask import Flask, redirect
import json

app = Flask(__name__) # Create our flask app

@app.route('/<string:inp>/') # Listen for the route
def request_data(inp):
    with open("urls.json", "r") as file: # Open the file
        data = json.load(file) # Read it with json and convert it to a dictionery

    url = data[inp] # Check the dictionery for the input

    if url is not None: # Check if it is in the file
        return redirect(url) # Redirect

if __name__ == '__main__':
    app.run(port=5050) # Run the app
