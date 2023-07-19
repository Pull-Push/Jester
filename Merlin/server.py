from flask_app import app
from flask_app.models import user_model
from flask_app.controllers import user_controller

if __name__ == "__main__":
    app.run(port=8008, debug=True)