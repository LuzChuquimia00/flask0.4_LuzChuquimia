from flask import Flask, send_file, render_template

app = Flask(__name__)
#
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

@app.route('/themes')
def songs():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    ask = """
            SELECT name FROM artists
            ORDER BY name DESC;
          """
    
    result = data_base.execute(ask)
    list_of_result = result.fetchall()
    
    return render_template("songs.html", songs=list_of_result) 