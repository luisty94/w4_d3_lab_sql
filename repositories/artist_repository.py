from db.run_sql import run_sql

from models.artist import Artist

#SELECT BY LIST (ALL)

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(
            row['name'],
            row['id']
            )
        artists.append(artist)
    return artists

# SAVE

def save(artist):
    sql = """INSERT INTO artists (name)
    VALUES (%s) RETURNING *
    """

    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

# SELECT

def select(id):
    artist = None
    sql = "SELECT * from artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist

# DELETE

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE ALL

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# UPDATE

def update(artist):
    sql = """UPDATE artist SET (name) = (%s) WHERE id = %s"""
    values = [artist.name, artist.id]
    run_sql(sql, values)

