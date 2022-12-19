from spotify import get_album, get_track


class Media:
    def __init__(self, id, title, release_year, href):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.href = href

    def summary(self):
        return f'"{self.title}" was released in {self.release_year}.\nView this media at {self.href}.'

    def __repr__(self):
        return f"Media: {self.title} - {self.release_year}"


class Song(Media):
    def __init__(self, id, title, release_year, href, explicit, duration_ms, disc_number, popularity):
        super().__init__(id, title, release_year, href)
        self.explicit = explicit
        self.disc_number = disc_number
        self.popularity = popularity
        self.duration_ms = duration_ms
        self.duration_mins = int(self.duration_ms) / 60000

    # We can override a method in the parent class be redefining it in the child class
    def summary(self):
        if (self.explicit):
            return f'The song "{self.title}" was released in {self.release_year}.\nListen on Spotify: {self.href}. Be careful, it\'s explicit.'
        else:
            return f'The song "{self.title}" was released in {self.release_year}.\nListen on Spotify: {self.href}'

    def how_long(self):
        if self.duration_mins > 10:
            return "That song is way too long!"
        elif self.duration_mins <= 10 and self.duration_mins > 5:
            return "That is a long song."
        elif self.duration_mins <= 5 and self.duration_mins > 2:
            return "That song is medium length"
        elif self.duration_mins <= 2:
            return "That is a short song."

    def __repr__(self):
        return f"Song: {self.title} - {self.release_year}"


if __name__ == '__main__':

    # the Media class can be used for any type of media
    # A music album is just one example
    # We could also use this class to represent books, movies, blog posts, etc.
    album = get_album('5BWl0bB1q0TqyFmkBEupZy')

    media = Media(album['id'], album['name'],
                  album['release_date'], album['external_urls']['spotify'])

    # print(album['id'])
    # print(album['name'])
    # print(album['release_date'])
    # print(album['external_urls']['spotify'])

# Using the class instantiation
    # print(media)
    # print(media.id)
    # print(media.title)
    # print(media.release_year)
    # print(media.href)
    # print(media.summary())

    # ------------------------------------------------------------------------#

    # We can create a child class that represents a more specific type of media
    # for example, a specific song on Spotify.com
    # We want this song to inherit all of the attributes of the parent
    # but also have additional attributes that are specific to the child class.

    track = get_track('75FEaRjZTKLhTrFGsfMUXR')

    song = Song(track['id'],
                track['name'],
                track['album']['release_date'],
                track['external_urls']['spotify'],
                track['explicit'],
                track['duration_ms'],
                track['disc_number'],
                track['popularity'])

    # print(song)
    # print(track['id'])
    # print(track['name'])
    # print(track['album']['release_date'])
    # print(track['external_urls']['spotify'])
    # print(track['explicit'])
    # print(track['duration_ms'])
    # print(track['disc_number'])
    # print(track['popularity'])

# Using the class instantiation
    # print(song)
    # print("id:", song.id)
    # print("Title:", song.title)
    # print("Release Year:", song.release_year)
    # print("Link:", song.href)
    # print("Explicit:", song.explicit)
    # print("Duration in Miliseconds:", song.duration_ms)
    # print("Duration in Minutes:", round(song.duration_mins, 2))
    # print("Disc Number:", song.disc_number)
    # print("Popularity:", song.popularity)
    # print(song.how_long())
    print(song.summary())
