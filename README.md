# Song-to-learn-application
Brief Project Description: Create a GUI for an application show what songs user learnt and not learn. The app also allow to add more song, sorting or mark as learnt
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
