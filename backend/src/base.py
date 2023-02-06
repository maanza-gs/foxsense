from flask import Flask

app = Flask(__name__)

@app.route('/profile')
def my_profile():
    response_body = {
        "Name": "Maanasa",
        "AboutMe" :"Full stack dev"
    }

    return response_body
