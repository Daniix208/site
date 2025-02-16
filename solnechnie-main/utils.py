import sqlite3

from flask import url_for


def get_planet_list_names():
    con = sqlite3.connect(f".{url_for('static', filename='data/data.db')}")

    SQL_SELECT = "SELECT name FROM planets"
    query = con.execute(SQL_SELECT)
    data = query.fetchall()
    data = [
        item[0] for item in data
    ]  # вытаскиваем имена из кортежей и делаем просто список строк

    return data


def get_planet_info_by_name(name):
    con = sqlite3.connect(f".{url_for('static', filename='data/data.db')}")

    SQL_SELECT = f"SELECT * FROM planets WHERE name = '{name}'"
    query = con.execute(SQL_SELECT)
    data = query.fetchone()

    return data
