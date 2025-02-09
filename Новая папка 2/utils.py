import sqlite3

def get_planets():
    con = sqlite3.connect('static/planets.db')
    query = con.execute('SELECT name from planets')
    data = query.fetchall()
    data = [item[0] for item in data]
    return data
