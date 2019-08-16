"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list.songs)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print(song_list.songs)
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs
song_list.sort_songs()
print(song_list.songs)
for i in range(len(song_list.songs)):
	print(song_list.songs[i])
# check manually if the list is ordered by artist or not (default)

# test adding a new Song
song_list.add_songs("Sugar", "Maroon 5", 2017)
song_list.sort_songs()
print(song_list.songs[0])
# The new song should be on top of the list (A, A, 1, True)
# As it has been added and sort by artist (default)

# test get_song()
print(song_list.get_songs("Heartbreak Hotel"))
# The result should be a whole song when it get called by its title
print(song_list.songs)
song_list.remove_songs(song_list.get_songs("Sugar"))
print(song_list.songs)
# Tesing remove_song func with get_song item

# test getting the number of required and learned songs (separately)
song_list.get_status_songs()
# Manually check, the result should be 2 learned and 4 required to learn (default)

# test saving songs (check CSV file manually to see results)
