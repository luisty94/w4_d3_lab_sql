from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository

#SELECT BY LIST (ALL)

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist'])
        album = Album(
            row['title'],
            artist,
            row['genre'],
            row['id']
            )
        albums.append(album)
    return albums

# SAVE

def save(album):
    sql_string = """INSERT INTO albums (title, artist, genre)
    VALUES (%s, %s, %s) RETURNING *
    """

    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql_string, values)
    id = results[0]['id']
    album.id = id
    return album

# SELECT

def select(id):
    album = None
    sql = "SELECT * from albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['artist'])
        album = Album(result['title'], artist, result['genre'], result['id'])
    return album

# DELETE

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# DELETE ALL

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

# UPDATE

def update(album):
    sql = """UPDATE albums SET (title, artist, genre) = (%s, %s, %s) WHERE id = %s"""
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)

