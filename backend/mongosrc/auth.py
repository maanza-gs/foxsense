from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db   ##means from __init__.py import db
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        inputDetail = {
            'username': request.json['username'],
            'password': request.json['password']
        }

        user = db.find_one({'username': inputDetail['username']})
        return jsonify({
            'username': user['username'],
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        inputDetail = {
            'username': request.json['username'],
            'password': request.json['password']
        }

        user = db.find_one({'username': inputDetail['username']})
        return jsonify({
            'username': user['username'],
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
