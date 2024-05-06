class Song:
    count = 0
    artists = []
    artist_count = {}
    genres = []
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            # If the genre count includes the key of genre and can be GOTTEN
            cls.genre_count[genre] += 1
            # Then SET genre_count dictionary[genre value] to increment by +1.
        else:
            cls.genre_count[genre] = 1
            # Otherwise, SET a new key value pair of [genre] and the value of 1.

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1