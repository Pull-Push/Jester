# all @app.routes go in here! 
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.controllers import room_controller


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/dashboard')
# def dash():
#     return render_template('dashboard.html')


@app.route('/new/user', methods=['POST'])
def register():
    info = request.form
    User.save_user(info)
    return redirect("/dashboard")

@app.route('/login/user', methods=['POST'])
def login():
    info = request.form
    if User.check_user(info):
        logger = User.check_user(info)
        if info['password'] == logger.password:
            print("success")
            return redirect("/dashboard")
    print("error")
    return render_template('index.html')
    