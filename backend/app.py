from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/thebookmark'
mongo =  PyMongo(app)

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)