from flask import Flask, send_file

app = Flask(__name__)
#
with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'
