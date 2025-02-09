from flask import Flask, url_for
from utils import get_planets

app = Flask(__name__)


@app.route("/") 
@app.route("/home")
def home_page():
    planets = get_planets()
    links_list = []
    for name in planets:
        links_list.append(
            f'<li class = "list-ground-item><a href = "/planet/{name}" class = "text-decoration-none">{name}<a/></li>'
        )
    links_str = " ".join(links_list)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Планеты</title>
</head>
<body>
    <div class="container">
        <div class="row mt-5">
            <h1>Планеты солнечной системы</h1>
            <div class="row">
                <div class="col-md-4">
                    <ul class="list-group">
                        {links_str}
                </div>
            </div>
        </div>
    </div>
</body>
</html>'''

@app.route("/space")
def space_page():
    return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Space</title>
          <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
          <h1>Планеты солнечной системы</h1>
          <img src="{url_for('static', filename='img/planets.jpg')}" alt="Изображение планет">
        </body>
        </html>
    """



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)
