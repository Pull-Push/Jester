from flask_app import app, socketio
from flask_app.controllers import user_controller

if __name__ == "__main__":
    socketio.run(app,port=8008, debug=True)
