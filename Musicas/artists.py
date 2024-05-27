from flask import Blueprint,render_template
from . import db 
bp = Blueprint('artists',__name__, url_prefix= '/artist')

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
        SELECT name FROM artists WHERE ArtistId = ?;
    """
    consulta2 = """
        SELECT AlbumId ,Title FROM albums WHERE ArtistId = ?;
    """
    
    res = con.execute(consulta1, (id,))#me quede aqui, continua con las fotos del celu.
    artists = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_musicas = res.fetchall()
    pagina = render_template('detalle_artist.html', 
                            artists=artists,   
                            musicas=lista_musicas)
    return pagina

@bp.route('/')
def artists():
    data_base = db.get_db() #Consigue la base de datos que estaba en db.py#
    ask = """
            SELECT name, ArtistId FROM artists
            ORDER BY name ASC;
          """
    
    result = data_base.execute(ask)
    list_of_result = result.fetchall()
    
    return render_template("artists.html", artists=list_of_result)
