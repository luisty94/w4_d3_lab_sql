import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Oasis')
artist_repository.save(artist_1)

album_1 = Album("Roll With It", artist_1, "Rock")
album_repository.save(album_1)
album_2 = Album("Another Album", artist_1, "Pop")
album_repository.save(album_2)

album_1.genre = "Pop"
album_repository.update(album_1)

artist_2 = Artist("David Bowie")
album_3 = Album("Rocket", artist_2, "Indie")
artist_repository.save(artist_2)
album_repository.save(album_3)

album_repository.delete(3)



for album in album_repository.select_all():
    print(album.__dict__)



pdb.set_trace()
