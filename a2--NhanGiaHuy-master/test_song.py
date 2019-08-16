"""(Incomplete) Tests for Song class."""

""" Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required

# test initial-value song
song2 = Song("One More Night", "Maroon 5", 2012, True)
# TODO: write tests to show this initialisation works
print(song2)
assert song2.artist == "Maroon 5"
assert song2.title == "One More Night"
assert song2.year == 2012
assert song2.is_required
# test mark_learned()
# TODO: write tests to show the mark_learned() method works
song2.mark_learned()
assert (song2.is_required == False)
