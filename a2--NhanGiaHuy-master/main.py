"""
Name:Nhan Gia Huy
Date:6/1/2019
Brief Project Description: Create a GUI for an application show what songs user
learnt and not learn. The app also allow to add more song, sorting or mark as
learnt
GitHub URL: https://github.com/NhanGiaHuy/Song-to-learn-application
"""

"""
Psuedo code
Song to learn app:
Initializing (def init(self))
	get all attributes from parent class (App)
	Create an empty list (called album)
	Pass in album to SongList class
	load song to album
	load review list (for kivy display purpose)

Building list of songs function 
(build a list of songs with 2 background for learn and unlearn song,
This list will be working with review list,
when press the unlearn song, mark it as learned, background change)
	<Build list of song for GUI>
	for each of the song in album review list
		if song is learned
			create a button with (text is string in the review list, background color is black)
		else song is unlearn
			create a button with (text is string in the review list, background color is grey)
			Set the id is song title
			bind mark_as_learned function when button is selected
		Create widget and add to the GUI

	<Mark_as_learned function>
	When the button is selected
		get the id (the id itself is the song title)
		pass the id in album get_song_by_title function to get the song
		marked that song as learned, return the data to album
		Reload review list from new changes made in album
		clear the list of songs on GUI
		rebuild the list with new review list
		update the main status: Song has been learned
		update number of unlearn and learn songs


Sorting function(Radio buttons and def sorting by radio buttons)
	Set value for each radio buttons (default will be artist)
	When any value is active, trigger sorting function, pass in option (as artist, year, or title)

	Sorting function(option):
		trigger album sorting function (from SongList class), pass in option
		load review list from new ordered album 
		Clear the list in GUI 
		Recreate the list with new ordered review list
		Update main status bar to Sorting by (option) 

Adding function(Gathering values and add new songs to album if conditions is filled)
	Gathering function:
	<For string>
		Get text from text input box from the GUI 
		Turn text into title form
		Return text
	<For number (integer)>
		try 
			get number as integer from text input box from the GUI 
			if number is bigger than 2019
				return "case number is > 2019"
			else return number
		when meet ValueError
			return "case number is error"

	Adding function
		get title by gathering string(title)
		get artist by gathering string(artist)
		get year by gathering number (year)
		if title is blank
			prompt the user to enter the title
		else if artist is blank
			prompt the user to enter the artist
		else if year is blank
			prompt the user to enter the year
		else if year is "Case number is error"
			prompt user to enter a number 
		else if year is negative (<0) 
			prompt user to enter a positive number
		else if year is "case number is > 2019"
			prompt user to enter a valid year 
		else 
			all the condition is filled
			triggering album add new song (from SongList)
			reload the review list (for display on GUI)
			clear the list on GUI
			Build the list on GUI
			Update new status: New song has been added
			Update number of new learn and unlearn songs


Build GUI func (def build(self))
	Start to build GUI from kivy language (from app.kv)
	Set the title to "Song To Learn by Nhan Gia Huy"
	Triggering createing album function
	Set main status bar to greet user 
	Update number of learn and unlearn songs
	Return GUI 

End program function(def on_stop(self))
	triggering album save song function, save all the data

"""

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.properties import StringProperty

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

from song import Song
from songlist import SongList
# Create your main program in this file, using the SongsToLearnApp class


class Song_To_LearnApp(App):
    # The string for main status will be change
    # depend on the function runs
    main_status = StringProperty()
    # The string the update when new song added or new song learnt
    learn_status = StringProperty()

    # Initializer and start to load songs from the file
    def __init__(self, **kwargs):
        super(Song_To_LearnApp, self).__init__(**kwargs)
        self.album = SongList()
        self.album.load_songs("songs.csv")
        self.album.kivy_load_songs()

    def count_status(self):
        self.learn_status = self.album.get_status_songs()

    # GUI BUILDER
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        self.title = "Song to learn v2.0 by Nhan Gia Huy"
        self.root = Builder.load_file("app.kv")
        # Create the album
        self.create_album()
        # Trigger learn status
        self.count_status()
        # Welcome user
        self.main_status = "Welcome to Song To Learn App"
        return self.root

    def on_stop(self):
        self.album.save_songs()

    # Generating an album based on the song list
    def create_album(self):
        # For every song in the list
        for song in self.album.review_list:
            # If it is learned, make the button background black
            if song.split(",")[1] == "learned":
                temp_text = "{} ({})".format(song.split(",")[0], song.split(",")[1])
                temp_button = Button(text=temp_text, background_color=(0, 0, 0, 1))
            # Else, make a button with a background of grey
            else:
                # Create a text for the button to help the user know the song
                temp_text = "{}".format(song.split(",")[0])
                # give the song title as an ID of the  button
                temp_id = song.split(",")[-1]
                # Create a button
                temp_button = Button(id=temp_id, text=temp_text)
                # bind the function to the button
                # when pressed, this will marked the song as learnt
                temp_button.bind(on_release=self.press_learnt)
            # Add the button the the box
            self.root.ids.list_of_songs.add_widget(temp_button)

    # Function when the button pressed, unlearn song return as learnt
    def press_learnt(self, instance):
        # When pressed, the selected button will throw its ID to the get song
        self.album.get_songs(instance.id).mark_learned()
        # recreate the list
        self.root.ids.list_of_songs.clear_widgets()
        self.album.kivy_load_songs()
        self.create_album()
        # Update status bar
        self.main_status = "{} has been marked as learnt".format(instance.text)
        # update learn status
        self.count_status()

    # Create a attribute for sorting radio button
    # default setup for the radio button (default will be sort by artist)
    Artist = ObjectProperty(True)
    Title = ObjectProperty(False)
    Year = ObjectProperty(False)

    #  sorting songs based on radio buttons
    def radio_button_sort(self, option):
        # Sort the song based on the option
        self.album.sort_songs(option=option)
        # Recreate list for GUI
        self.album.kivy_load_songs()
        # Destroy the whole list and recreate it with new order (sorted)
        self.root.ids.list_of_songs.clear_widgets()
        self.create_album()
        # Update status bar
        self.main_status = "Sorting by {}".format(option)

    # function to open the popup for adding purpose
    def open_adding_pop_up(self):
        self.root.ids.Adding_Popup.open()
        # Update status bar
        self.main_status = "Adding new song"

    # Function to dismiss the popup
    def press_cancel_pop_up(self):
        # Dismiss the pop up
        self.root.ids.Adding_Popup.dismiss()
        # Update count learn song
        self.count_status()

    # Handle add function
    def press_add(self):
        # gather information for new song
        title = self.get_title()
        year = self.get_year()
        artist = self.get_artist()
        # check the information
        # Title is blank => Prompt title shouldnt be blank
        if title == "" or title == " ":
            self.root.ids.add_prompt_3.text = "Title cannot be blank"
        # artist is blank => Prompt artist shouldnt be blank
        elif artist == "" or artist == " ":
            self.root.ids.add_prompt_3.text = "Artist cannot be blank"
        # Year is blank => Prompt artist shouldnt be blank
        elif year == "" or year == " ":
            self.root.ids.add_prompt_3.text = "Year cannot be blank"
        # If year get return as -1, There is a Value Error, Prompt the Error
        elif year == "Case value":
            self.root.ids.add_prompt_3.text = "Invalid input for year. Try again"
        # If the year is unreal, prompt the user to input again
        elif year == "Case 2019":
            self.root.ids.add_prompt_3.text = "The year is unreal, must be =< 2019"
        # If year is negative, Prompt year must be > 0
        elif year < 0:
            self.root.ids.add_prompt_3.text = "The year must be > 0"
        else:
            # add new song to the list
            self.album.add_songs(title, artist, year)
            # clear and recreate the list
            self.root.ids.list_of_songs.clear_widgets()
            self.album.kivy_load_songs()
            self.create_album()
            # close popup
            self.root.ids.Adding_Popup.dismiss()
            # Update status bar
            self.main_status = "{} by {} ({}) has been added".format(title, artist, year)
            # update learn status
            self.count_status()

    # Method to gather the information in the text input box
    def get_title(self):
        # retrieve value and return value
        value = str(self.root.ids.add_detail_title.text).title()
        return value

    def get_artist(self):
        # retrieve value and return value
        value = str(self.root.ids.add_detail_artist.text).title()
        return value

    def get_year(self):
        # retrieve value and return value
        try:
            value = int(self.root.ids.add_detail_year.text)
            if value > 2019:
                return "Case 2019"
            else:
                return value
        # return Case value for case where input is a Value Error
        except ValueError:
            return "Case value"

Song_To_LearnApp().run()
