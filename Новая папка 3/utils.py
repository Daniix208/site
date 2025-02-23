import sqlite3


def create_db():
    """
        Создает базу данных и таблицы, если они еще не существуют.
    """
    con = sqlite3.connect("films.db")

    SQL_CREATE = """
    CREATE TABLE IF NOT EXISTS films (
      id INTEGER PRIMARY KEY,
      title STRING,
      rating REAL,
      description TEXT,
      year INTEGER,
      poster TEXT, 
      genres TEXT,
      country TEXT,
      duration INTEGER,
      description TEXT,
      age_rating INTEGER,
      trailer_url TEXT
    )
    """
    con.execute(SQL_CREATE)


def get_all_films():
    """
    Получает из БД id, название, URL постера и короткое описание для каждого фильма.
    Возвращает список фильмов в виде словарей
    """
    con = sqlite3.connect("films.db")

    SQL_SELECT = """
        SELECT id, title, poster, country, year, rating FROM films
    """
    query = con.execute(SQL_SELECT)
    row_data = query.fetchall()

    data = []
    for row in row_data:
        film = {}
        film["id"] = row[0]
        film["title"] = row[1]
        film["poster"] = row[2]
        film["country"] = row[3]
        film["year"] = row[4]
        film["rating"] = row[5]
        data.append(film)
    return data


def get_film_by_id(id):
    """
    Поиск фильма в БД по его ID.
    Функция возвращает полную информацию о фильме в виде словаря.
    """
    con = sqlite3.connect("films.db")

    SQL_SELECT = f"""
        SELECT * FROM films WHERE id = {id}
    """
    query = con.execute(SQL_SELECT)
    row_data = query.fetchone()

    data = {
        "id": row_data[0],
        "title": row_data[1],
        "year": row_data[2],
        "genres": row_data[3],
        "country": row_data[4],
        "description": row_data[5],
        "duration": row_data[6],
        "rating": row_data[7],
        "age_rating": row_data[8],
        "poster": row_data[9], 
    }
    return data


def add_film(data):
    """
    Принимает данные фильм и добавляет его в БД.
    """
    title = data["title"]
    rating = data["rating"]
    description = data["description"]
    year = data["year"]
    poster = data["poster"]
    genres = data["genres"]
    country = data["country"]
    duration = data["duration"]
    description = data["description"]
    age_rating = data["age_rating"]
    trailer_url = data["trailer_url"]

    con = sqlite3.connect("films.db")

    SQL_INSERT = f"""
        INSERT INTO films(title, rating, description, year, poster, genres, country, duration, description, age_rating, trailer_url)
        VALUES ('{title}',{rating},'{description}',{year},'{poster}','{genres}','{country}',{duration},'{description}',{age_rating},'{trailer_url}')
    """

    con.execute(SQL_INSERT)
    con.commit()