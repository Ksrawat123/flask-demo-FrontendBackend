#import the requied things to be use
from flask import Flask, request, redirect, url_for
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
  
# Load environment variables
load_dotenv()

# MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client.dummydb
collection = db['dummydb']

# Flask app
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data Submitted Successfully'
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9000,debug=True)