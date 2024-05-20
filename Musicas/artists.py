from flask import Blueprint,render_template
from . import db 
bp = Blueprint('artists',__name__, url_prefix= '/artist')

@bp.route('/')
def artists():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    ask = """
            SELECT name FROM artists
            ORDER BY name ASC;
          """
    
    result = data_base.execute(ask)
    list_of_result = result.fetchall()
    
    return render_template("artists.html", artists=list_of_result)
