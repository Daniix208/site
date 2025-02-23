from flask import Flask, render_template
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
    films = get_all_films()
    return render_template('index.html', films = films)

@app.route("/films/<int:film_id>")
def film_page(film_id):
   film_data = get_film_by_id(film_id)
   return render_template("film.html", film = film_data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug = True)