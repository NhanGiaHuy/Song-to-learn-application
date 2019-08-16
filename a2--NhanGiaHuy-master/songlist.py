# create your SongList class in this file


import csv
from operator import attrgetter
from song import Song


class SongList:
    def __init__(self):
        # Create a empty list to put song data in
        self.songs = []
        # Create another list for display purposes
        self.review_list = []

    def __repr__(self):
        for i in range(len(self.songs)):
            print(self.songs[i])
            return

    def load_songs(self, file):
        # Open the file
        csv_file = open(file)
        # Read the file
        reader = csv.reader(csv_file)
        # Turn the data into the list
        list_of_song = list(reader)
        # For each of the song in the list, turn "y" to True and "n" to False, change year from string into number
        for i in range(len(list_of_song)):
            if list_of_song[i][-1] == "y":
                list_of_song[i][-1] = True
            else:
                list_of_song[i][-1] = False
            list_of_song[i][2] = int(list_of_song[i][2])
            # Append each song into Song class then append into the song list
            self.songs.append(Song(list_of_song[i][0], list_of_song[i][1], list_of_song[i][2],list_of_song[i][3]))
        # close the file
        csv_file.close()
        # Return the new song list
        return self.songs

    def sort_songs(self, option="artist"):  # Sorting song list based on passing key into to the function
        return self.songs.sort(key=attrgetter(option))  # Return new ordered song list

    def add_songs(self, title='', artist='', year=0):  # add new song
        new_song = Song(title, artist, year)  # Append title, artist, year to Song as new_song
        self.songs.append(new_song)  # Add new_song into song list
        # prompt user that the song has been added
        print("{} by {} ({}) has been added".format(new_song.title,
                                                    new_song.artist, new_song.year))  #
        # return new song list
        return self.songs

    def get_songs(self, get_title=""):  # get song by title
        # for every song in the list, if song title is same as title, return that song
        for song in self.songs:
            if song.title == get_title:
                return song

    def get_status_songs(self):  # get number of learn song and unlearn song
        # count learned song, then count unlearn songs by getting the difference in total and learnt song
        count_learned_song = 0
        # for every learnt song, plus 1 to the count_learned_song
        for song in self.songs:
            if song.is_required:
                count_learned_song += 1
        # Return a prompt where state learned song and unlearn song
        return '{} song(s) learned and {} song(s) required to learn'.format(count_learned_song,
                                                                            len(self.songs) - count_learned_song)

    def save_songs(self):  # save songs in a specific format
        # import all the data from song list to save_list
        save_list = self.songs
        # open the file and ready to write
        f = open("songs.csv", "w")
        # for every song in save_list, start to format the data into specific format
        for song in save_list:
            if song.is_required:
                song.is_required = "y"
            else:
                song.is_required = "n"
            # write the data into the file
            f.write("{}\n".format(song))
        f.close()  # close that file

    # kivy_load_song is a function that change the songs list into format to use with Kivy
    def kivy_load_songs(self):  # this function will work with review_list created at first
        # refresh the review_list and start to modify based on the song list
        self.review_list = []
        # for every song in song list, start to format the song data, in order to work with kivy GUI
        for song in self.songs:
            if not song.is_required:
                self.review_list.append("{} by {} in {},learned,{}".format(song.title,
                                                                           song.artist, song.year, song.title))
            else:
                self.review_list.append("{} by {} in {},,{}".format(song.title,
                                                                    song.artist, song.year, song.title))
        # return review_list
        return self.review_list

    # extra functions
    def remove_songs(self, get_songs_func):
        return self.songs.remove(get_songs_func)

    def edit_songs(self, get_songs_func):
        get_songs_func.title = str(input("Enter new title of the song: "))
        get_songs_func.artist = str(input("Enter new artist name of the song: "))
        get_songs_func.year = str(input("Enter new year released of the song: "))
        return get_songs_func
