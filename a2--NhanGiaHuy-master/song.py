# create your Song class in this file
class Song:
    # class Song will take in 4 attributes: title, artist, year and is_required
    def __init__(self, title='', artist='', year=0, is_required=True):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = is_required

    def __str__(self):
        return ("{}, {}, {}, {}"). \
            format(self.title, self.artist, self.year, self.is_required)

    def __repr__(self):
        return ("{}, {}, {}, {}"). \
            format(self.title, self.artist, self.year, self.is_required)
    # function that mark learnt for song
    # If the song is learnt, the function will return song has been learnt
    def mark_learned(self):
        if self.is_required == False:
            print("Song has been learned")
        else:
            self.is_required = False
            return self.is_required
