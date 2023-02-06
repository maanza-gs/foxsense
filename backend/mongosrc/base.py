from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/thebookmark'
mongo =  PyMongo(app)

CORS(app)

db = mongo.db.users

# @app.route('/')
# def index():
#     return "<h3>Hi there, I'm Maanasa!</h3>"

# @app.route('/users',methods=["POST"])
# def createUser():
#     db.insert({
#         'username': request.json['username'],
#         'name': request.json['name'],
#         'email': request.json['email'],
#         'password': request.json['password']
#     })
#     return jsonify({'id': str(ObjectId(id)), 'msg':'User Created Successfully'})

# @app.route('/users', methods=['GET'])
# def getUsers():
#     users=[]
#     for doc in db.find():
#         users.append({
#             '_id': str(ObjectId(doc['_id'])),
#             'username': doc['username'],
#             'name': doc['name'],
#             'email': doc['email'],
#             'password': doc['password']
#         })

#     return jsonify(users)

# if __name__ == '__main__':
#     app.run(debug=True)

@app.route('/profile')
def my_profile():
    response_body = {
        "Name": "Maanasa",
        "AboutMe" :"Full stack dev"
    }

    return response_body
