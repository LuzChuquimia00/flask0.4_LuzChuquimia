from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

#@app.route('/bye')
#def bye():
#    return 'Goodbye'

#@app route('/favicon.ico')
#def favicon():
#    return send_file('static/favicon.ico') 

from . import artists
app.register_blueprint(artists.bp)


