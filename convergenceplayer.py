# Convergence Jukebox is Python based codes that emulates a Jukebox and plays mp3 media
# Copyright (C) 2012 by Brad Fortner
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses.
# The authour can be reached via www.convergencejukebox.com
# Convergence Jukebox employs the hsaudiotag Python library which is released under an OSI BSD licence.
# hsaudiotag see: https://pypi.python.org/pypi/hsaudiotag
# Convergence Jukebox employs the playmp3.py Python library for windows Copyright (c) 2011 by James K. Lawless
# playmp3.py has been released under an MIT / X11 licence. See: http://www.mailsend-online.com/license.php.

import os
import glob
import datetime  # Used to convert song duration in seconds to minutes/seconds.
import random
import time  # Used in time_date_stamp. http://bit.ly/1MKPl5x and http://bit.ly/1HRKTMJ
import pickle  # Used to save and reload python lists
import sys  # Used for testing new code. Required to add sys.exit().
from hsaudiotag import auto  # Used to work with MP3 ID3 data https://pypi.python.org/pypi/hsaudiotag
from ctypes import *  # Used by playmp3.py windows based mp3 player http://bit.ly/1MgaGCh
import csv
import getpass  # Used to get user name http://stackoverflow.com/questions/4325416/how-do-i-get-the-username-in-python
import re  # Used in searching Genre substrings. Specifically word-boundaries of regular expressions.
from Tkinter import *  # Used as message to alert users to place MP3's in music folder

computer_account_user_name = getpass.getuser()
genre_file_changed = ""
random_change_list = ""
#got_artist = ""  # Used to select Artist in random play routine
selectedArtists = []  # Used to select multiple artists in random play routine
artistSelectRoutine = 0  # Used to break Artist
artistSortRequired = "No"
genreYearSort = "No"
artistSortRequiredByYear = "No"
winmm = windll.winmm  # required by playMP3
play_list = []  # Holds song numbers for paid selections.
build_list = []  # List temporarily holds ID3 data during song processing. Data later written to song_list then cleared.
remove_list = []  # Python List used to remove songs from random_list
random_list = []
flag_fourteen = ""
flag_fourteen_change = ""
output_list = []  # List is used to output information related to Jukebox functions. Contains information on songs
song_list = []  # List is used to build final list of all songs including ID3 information and file location.
# song_list info locations: songTitle = song_list[x][0], songArtist = song_list[x][1], songAlbum = song_list[x][2]
# song_year = song_list[x][3], songDurationSeconds = song_list[x][4], songGenre = song_list[x][5],
# songDurationTime = song_list[x][6], songComment = song_list[x][7]

def set_up_user_files_first_time():

    global full_path
    full_path = os.path.realpath('__file__')  # http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    artist_list =[]

    if os.path.exists(str(os.path.dirname(full_path)) + "\music"):
        print "music directory exists. Nothing to do here."
    else:
        print "music directory does not exist."
        os.makedirs(str(os.path.dirname(full_path)) + "\music")
        print "Program Stopped. Please place some mp3's in the Convergence Jukebox music directory and then re-run the software"
        master = Tk()
        whatever_you_do = "Program Stopped. Please place some mp3's in the Convergence Jukebox music directory and then re-run the software"
        msg = Message(master, text = whatever_you_do)
        msg.config(bg='white', font=('times', 24, 'italic'), justify = 'center')
        msg.pack()
        mainloop( )
        #sys.exit()

    if os.path.exists("log.txt"):
        print "log.txt exists. Nothing to do here."
    else:
        log_file = file("log.txt", "w")
        log_file.close()
        print "log.txt created."

    if os.path.exists("genre_flags.txt"):
        print "genre_flags.txt exists. Nothing to do here."
    else:
        genre_file = file("genre_flags.txt", "w")
        genre_file.write("null,null,null,null,null,Starting Year,Ending Year,Select Artists A thru C,Select Artists D thru H,Select Artists I Thru M,Select Artists N Thru R,Select Artists S Thru V,Select Artists W Thru Z,Wednesday December 16 2015 12:44:11 PM")
        genre_file.close()
        print "genre_flags.txt created."

    if os.path.exists("file_count.txt"):
        print "file_count.txt exists. Nothing to do here."
    else:
        old_file_count = file("file_count.txt", "w")
        old_file_count.write("0")
        old_file_count.close()
        print "file_count.txt created."

    if os.path.exists("song_list.pkl"):
        print "song_list.pkl exists. Nothing to do here."
    else:
        song_list_file_create = file("song_list.pkl", "wb")
        song_list_file_create.close()
        print "song_list.pkl created."

    if os.path.exists("output_list.pkl"):
        print "output_list.pkl exists. Nothing to do here."
    else:
        output_list_file_create = file("output_list.pkl", "wb")
        output_list_file_create.close()
        print "output_list.pkl created."

    if os.path.exists("play_list.pkl"):
        print "play_list.pkl exists. Nothing to do here."
    else:
        play_list_file_create = open('play_list.pkl', 'wb')
        pickle.dump(play_list, play_list_file_create)
        play_list_file_create.close()
        print "play_list.pkl created."

    if os.path.exists("upcoming_list.pkl"):
        print "upcoming_list.pkl exists. Nothing to do here."
    else:
        upcoming_list_file_create = open('upcoming_list.pkl', 'wb')
        pickle.dump(upcoming_list, upcoming_list_file_create)
        upcoming_list_file_create.close()
        print "upcoming_list.pkl created."

    if os.path.exists("artist_list.pkl"):
        print "artist_list.pkl exists. Nothing to do here."
    else:
        artist_list_file_create = open('artist_list.pkl', 'wb')
        pickle.dump(artist_list, artist_list_file_create)
        artist_list_file_create.close()
        print "artist_list.pkl created."

    if os.path.exists("genre_last_timestamp.txt"):
        print "genre_last_timestamp.txt exists. Nothing to do here."
    else:
        genre_last_timestamp_file = file("genre_last_timestamp.txt", "w")
        #genre_last_timestamp_file.write("Wednesday December 16 2015 12:44:11 PM")
        genre_last_timestamp_file.close()
        print "genre_last_timestamp_file created."
        

def write_jukebox_startup_to_log():
    time_date_stamp = datetime.datetime.now().strftime("%A. %d. %B %Y %I:%M%p")  # time_date_stamp. bit.ly/1MKPl5x

    log_file_entry = open("log.txt", "a+")
    log_file_entry.write(str(time_date_stamp + ',' + 'Jukebox Started For Day' + ',' + '\n'))
    log_file_entry.close()
    # print computer_account_user_name.lower()


def genre_read_and_select_engine():  # Opens and reads genreFlags.csv file. Assigns genres to random play functionality.

    print "Entering genre_read_and_select_engine()."

    # Convergence Jukebox Function
    # Purpose is to look up genre_flags.txt file and assigns genres to random play functionality.
    # Videos to understand functions, variables, global variables, scopes and lists at http://bit.ly/1Qx32aW

    global flag_one  # Global variables created.
    global flag_two
    global flag_three
    global flag_four
    global flag_five
    global flag_six
    global flag_seven
    global flag_eight
    global flag_nine
    global flag_ten
    global flag_eleven
    global flag_twelve
    global flag_thirteen
    global flag_fourteen
    global flag_fourteen_change

    genre_file_open = open("genre_flags.txt", 'r+')
    to_be_split = genre_file_open.read()
    print "genre_flags.txt file contains: ", to_be_split
    genre_file_open.close()
    flag_file_input = to_be_split.split(",") # Split function explained at http://www.dotnetperls.com/split-python.

    if flag_file_input[0] == "null":  # flag_one assigned.
        flag_one = "none"
    else:
        flag_one = flag_file_input[0]
    if flag_file_input[1] == "null":  # flag_two assigned.
        flag_two = ""
    else:
        flag_two = flag_file_input[1]
    if flag_file_input[2] == "null":  # flag_three assigned.
        flag_three = ""
    else:
        flag_three = flag_file_input[2]
    if flag_file_input[3] == "null":  # flag_four assigned.
        flag_four = ""
    else:
        flag_four = flag_file_input[3]
    if flag_file_input[4] == "null":  # flag_five assigned.
        flag_five = ""
    else:
        flag_five = flag_file_input[4]
    if flag_file_input[5] == "Starting Year":  # flag_six assigned.
        flag_six = "null"
    else:
        flag_six = flag_file_input[5]
    if flag_file_input[6] == "Ending Year":  # flag_seven assigned.
        flag_seven = "null"
    else:
        flag_seven = flag_file_input[6]
    if flag_file_input[7] == "Select Artists A thru C":  # flag_eight assigned.
        flag_eight = "null"
    else:
        flag_eight = flag_file_input[7]
    if flag_file_input[8] == "Select Artists D thru H":  # flag_nine assigned.
        flag_nine = "null"
    else:
        flag_nine = flag_file_input[8]
    if flag_file_input[9] == "Select Artists I Thru M":  # flag_ten assigned.
        flag_ten = "null"
    else:
        flag_ten = flag_file_input[9]
    if flag_file_input[10] == "Select Artists N Thru R":  # flag_eleven assigned.
        flag_eleven = "null"
    else:
        flag_eleven = flag_file_input[10]
    if flag_file_input[11] == "Select Artists S Thru V":  # flag_twelve assigned.
        flag_twelve = "null"
    else:
        flag_twelve = flag_file_input[11]
    if flag_file_input[12] == "Select Artists W Thru Z":  # flag_thirteen assigned.
        flag_thirteen = "null"
    else:
        flag_thirteen = flag_file_input[12]
    flag_fourteen = flag_file_input[13]  # flag_fourteen assigned.
    flag_fourteen_change = flag_fourteen  # flag_fourteen_change assigned.


def basic_random_list_generator():
    global random_list_with_year
    if not song_list:
        print "Error - No song_list in basic_random_list_generator() to develop basic random_list"
    random_list_with_year = []
    year_builder = []
    print "Building Random List"
    y = 0
    zz = len(song_list)
    z = zz - 1
    while y <= z:  # ##########code to build random_list_with_year starts here.##########
        test_string = str(song_list[y][7])
        norandom_check = "norandom"
        if re.search(r'\b' + norandom_check + r'\b', test_string):  # regex word boundaries http://bit.ly/1lSLXeP

            log_file_update = open("log.txt", "a+")  # new song_list added to log file.
            log_file_update.write(str("Song " + str(song_list[y][1]) + " " + str(song_list[y][2]) \
                              + " has not been added to random_list because it's marked norandom." + '\n'))
            log_file_update.close()
            #sys.exit()
            y += 1
        else:
            random_list.append(y)  # adds song number to random_list
            song_number = song_list[y][9]  # assigns song number from song_list to song_number variable
            song_year = song_list[y][3]  # assigns song year from song_list to song_year variable
            year_builder.append(song_number)  # appends song_number to year_builder list
            year_builder.append(song_year)  # appends song_year to year_builder list
            random_list_with_year.append(year_builder)  # appends year_builder List to random_list_with_year
            year_builder = []  # clears year_builder list
            y += 1
            #  ##########code to build random_list_with_year ends here##########

    return random_list


def count_number_mp3_songs():
    print "Entering count_number_mp3_songs()"
    global last_file_count_a
    global current_file_count
    global last_file_count
    mp3_counter = 0
    full_path = os.path.realpath('__file__')

    mp3_counter = len(glob.glob1(str(os.path.dirname(full_path)) + "\music", "*.mp3"))  # Counts number of MP3 files in library
    current_file_count = int(mp3_counter)  # provides int output for later comparison
    if int(mp3_counter) == 0:
        print "Program Stopped. Please place some mp3's in the Convergence Jukebox music directory and then re-run the software"
        master = Tk()
        whatever_you_do = "Program Stopped. Please place some mp3's in the Convergence Jukebox music directory and then re-run the software"
        msg = Message(master, text = whatever_you_do)
        msg.config(bg='white', font=('times', 24, 'italic'))
        msg.pack()
        mainloop( )
        sys.exit()

    past_mp3_file_count = open("file_count.txt", "r")  # Looks at number mp3 files from last run and looks for a difference
    for last_file_count_a in past_mp3_file_count:
        print "The last time the Jukebox was run there were " + str(last_file_count_a) + " files on it."
    past_mp3_file_count.close()
    last_file_count = int(last_file_count_a)  # Variable holding count of mp3 songs from last time Jukebox was run.
    print "Exiting count_number_mp3_songs()"


def song_list_generator():
    global song_list
    print "Entering song_list_generator()"
    if last_file_count == current_file_count:  # If matched the song_list is loaded from file
        print "Jukebox music files same as last startup. Using existing song database."  # Message to console.
        song_list_recover = open('song_list.pkl', 'rb')  # Loads song_list
        song_list_open = pickle.load(song_list_recover)
        song_list_recover.close()
        song_list = song_list_open
    else:  # New song_list, filecount and location_list generated and saved.
        song_list_generate = []
        build_list = []
        time_date_stamp = datetime.datetime.now().strftime("%A. %d. %B %Y %I:%M%p")  # Timestamp generate bit.ly/1MKPl5x
        log_file_entry = open("log.txt", "a+")  # new song_list added to log file.
        log_file_entry.write(str(time_date_stamp + ',' + 'New song_list generated' + ',' + '\n'))
        log_file_entry.close()
        file_count_update = open("file_count.txt", "w+")  # Writes new filecount to filecount.txt file for next jukebox start.
        s = str(current_file_count)
        file_count_update.write(s)
        file_count_update.close()

        location_list = []  # Creates temporary location_list used for initial song file names for mp3 player.
        # File names later inserted in song_list to be used to play mp3's
        full_path = os.path.realpath('__file__')
        for name in os.listdir(str(os.path.dirname(full_path)) + "\music" + "\\"):  # Reads all files in the /music directory
            if name.endswith(".mp3"):  # If statement searching for files with mp3 designation
                title = name  # Name of mp3 transferred to title variable
                location_list.append(title)  # Name of song appended to location_list
        x = 0  # hsaudiotag 1.1.1 code begins here to pull out ID3 information
        while x < len(location_list):  # Python List len function http://docs.python.org/2/library/functions.html#len
            myfile = auto.File(str(os.path.dirname(full_path)) + "\music" + "\\" + location_list[x] + "")  # NOTE "" Quotes Required.
            #  hsaudiotag function that assigns mp3 song to myfile object
            titleorg = myfile.title  # Assigns above mp3 ID3 Title to titleorg variable
            artistorg = myfile.artist  # Assigns above mp3 ID3 Artist to artistorg variable
            albumorg = myfile.album  # Assigns above mp3 ID3 Album name to albumorg variable
            yearorg = myfile.year  # Assigns above mp3 ID3 Year info to yearorg variable
            durationorgseconds = myfile.duration  # Assigns mp3 Duration (in seconds) info to durationorgseconds var.
            genreorg = myfile.genre  # Assigns above mp3 Genre info to genreorg variable
            commentorg = myfile.comment  # Assigns above mp3 Comment info to commentorg variable
            title = str(titleorg)  # Removes Unicode "u" from string I think. http://bit.ly/1Qph2mS
            build_list.append(title)  # Title of song appended to build_list
            artist = str(artistorg)  # Removes Unicode "u" from string I think. http://bit.ly/1Qph2mS
            build_list.append(artist)  # Artist of song appended to build_list
            album = str(albumorg)  # Removes Unicode "u" from string I think. http://bit.ly/1Qph2mS
            build_list.append(album)  # Album title of song appended to build_list
            year = str(yearorg)  # Removes Unicode "u" from string I think. http://bit.ly/1Qph2mS
            build_list.append(year)  # Year of song appended to build_list
            durationseconds = str(durationorgseconds)  # Removes Unicode "u" from string
            build_list.append(durationseconds)  # Duration of song in seconds appended to build_list
            genre = str(genreorg)  # Removes Unicode "u" from string I think. http://bit.ly/1Qph2mS
            build_list.append(genre)  # Genre of song appended to build_list
            durationtimefull = str(datetime.timedelta(seconds=durationorgseconds))  # Info at http://bit.ly/1L5pU9t
            durationtime = durationtimefull[3:7]  # Slices string to minute:second notation. http://bit.ly/1QphhOW
            build_list.append(durationtime)  # Time of song in minutes/seconds of song appended to build_list
            comment = str(commentorg)  # Removes Unicode "u" from string I think. http://bit.ly/1Qph2mS
            build_list.append(comment)  # Comment in ID3 data appended to build_list
            full_file_name = str(location_list[x])
            build_list.append(full_file_name)
            song_list_generate.append(build_list)
            build_list.append(x)
            build_list = []
            y = len(location_list) - x
            print "Building play_list. Processing " + str(full_file_name) + ". " + str(y) + " files remaining to process."
            x += 1
        print len(song_list_generate)

        song_list_save = open('song_list.pkl', 'wb')  # song_list saved as binary pickle file
        pickle.dump(song_list_generate, song_list_save)
        song_list_save.close()

        song_list = song_list_generate
    print "Exiting song_list_generator()"
    return song_list


def play_random_song():
    mode = "Mode: Playing Song"
    print "Title: " + title
    print "Artist: " + artist
    print "Album: " + album
    print "Year Released: " + year + " Time: " + time
    output_prep_list = []
    output_list = []
    output_prep_list.append(title)
    output_prep_list.append(artist)
    output_prep_list.append(year)
    output_prep_list.append(time)
    output_prep_list.append(album)
    output_prep_list.append(mode)
    output_list.append(output_prep_list)
    output_list_save = open('output_list.pkl', 'wb')
    pickle.dump(output_list, output_list_save)
    output_list_save.close()
    time_date_stamp = datetime.datetime.now().strftime("%A. %d. %B %Y %I:%M%p")

    log_file_entry = open("log.txt", "a+")
    log_file_entry.write(str(time_date_stamp + ',' + str(song_list[x][8]) + ',' + str(mode) + ',' + '0' + '\n'))
    log_file_entry.close()

    full_path = os.path.realpath('__file__')
    print "Now playing: " + str(x)
    playMP3(str(os.path.dirname(full_path)) + '\music' + '\\\\' + song_list[x][8])  # Plays song using mp3Play.
    # info on mp3Play at http://www.mailsend-online.com/blog/play-mp3-files-with-python-on-windows.html
    # info at https://en.wikibooks.org/wiki/Python_Programming/Lists#Removing


def random_delete_song():
    print "Entering random_delete_song():"
    # next four lines write jukebox startup to log.txt
    # Timestamp info at http://stackoverflow.com/questions/13890935/timestamp-python
    time_date_stamp = datetime.datetime.now().strftime("%A. %d. %B %Y %I:%M%p")

    log_file_entry = open("log.txt", "a+")
    log_file_entry.write(str(time_date_stamp + ',' + 'Skipped norandom song: ' + str(song_list[x][8]) + '\n'))
    log_file_entry.close()

    del random_list[0]  # Deletes (removes) first element (song just played) from random_list.
    print "Leaving random_delete_song():"


def play_list_loader():
    global play_list

    play_list_recover = open('play_list.pkl', 'rb')  # Loads play_list.
    play_list = pickle.load(play_list_recover)
    play_list_recover.close()

    print play_list
    return play_list


def play_list_player():
    global play_list
    # This statement runs songs in play_list, deletes first song in play_list after it completes
    #  playing song and finally opens play_list to see if any new songs have appeared.
    print "Entering play_list_player():"
    print "Song in play_list: " + str(play_list[0])
    x = play_list[0]
    print x
    print  # x variable used below to print song data to screen
    title = str(song_list[x][0])
    artist = str(song_list[x][1])
    album = str(song_list[x][2])
    year = (song_list[x][3])
    time = (song_list[x][6])
    song_number = song_list[x][9]
    mode = "Mode: Playing Selected Song"
    print "Title: " + title
    print "Artist: " + artist
    print "Album: " + album
    print "Year Released: " + year + " Time: " + time
    output_prep_list = []
    output_list = []
    output_prep_list.append(title)
    output_prep_list.append(artist)
    output_prep_list.append(year)
    output_prep_list.append(time)
    output_prep_list.append(album)
    output_prep_list.append(mode)
    output_list.append(output_prep_list)
    output_list_save = open('output_list.pkl', 'wb')
    pickle.dump(output_list, output_list_save)
    output_list_save.close()
    time_date_stamp = datetime.datetime.now().strftime("%A. %d. %B %Y %I:%M%p")

    log_file_entry = open("log.txt", "a+")
    comma_removal = str(song_list[x][8])
    comma_free_title = comma_removal.replace(',', '')  # http://bit.ly/1SuAnRh
    log_file_entry.write(str(time_date_stamp + ',' + str(comma_free_title) + ',' + str(mode) + ',' + '1' + '\n'))
    log_file_entry.close()

    del comma_free_title
    del comma_removal
    upcoming_list_recover = open('upcoming_list.pkl', 'rb')
    upcoming_list = pickle.load(upcoming_list_recover)
    upcoming_list_recover.close()
    if len(upcoming_list) > 0:
        del upcoming_list[0]
    upcoming_list_save = open('upcoming_list.pkl', 'wb')
    pickle.dump(upcoming_list, upcoming_list_save)
    upcoming_list_save.close()

    if song_number in random_list:  # Removes paid songs from random_list. Checks for song number is in random_list.
        song_index = random_list.index(song_number)  # Index number assigned to variable. bit.ly/20FsVsl
        delete_song_index = random_list[song_index]  # Variable assigned to song number song number to be deleted.
        if song_number == delete_song_index:  # Checks if song to be deleted is still in random_list
            del random_list[song_index]  # Deletes song number from random list if found. http://bit.ly/1MRbT6I
    full_path = os.path.realpath('__file__')
    playMP3(str(os.path.dirname(full_path)) + '\music' + '\\\\' + song_list[x][8])  # Plays song using mp3Play.
    #  Info on mp3Play at http://bit.ly/1MgaGCh
    play_list_recover = open('play_list.pkl', 'rb')
    play_list = pickle.load(play_list_recover)
    play_list_recover.close()
    del play_list[0]
    play_list_save = open('play_list.pkl', 'wb')
    pickle.dump(play_list, play_list_save)
    play_list_save.close()
    if len(play_list) > 0:  # Checks for any paid songs to play
        play_list_player()  # Plays paid songs
    print "Exiting play_list_player():"


def random_mode_playback():
    print "The play_list is empty. Operating in random mode."
    x = random_list[0]  # First element in random_list assigned to x variable
    print len(random_list)
    title = str(song_list[x][0])
    artist = str(song_list[x][1])
    album = str(song_list[x][2])
    year = (song_list[x][3])
    time = (song_list[x][6])
    randomplay = str(song_list[x][7])
    play_random_song()
    del random_list[0]
    return random_list


def genre_file_change_detector():
    global random_list
    global computer_account_user_name
    print computer_account_user_name
    f = open('genre_last_timestamp.txt', 'r+')  # Reading timestamp.txt file
    genre_last_timestamp = f.read()
    f.close()

    f = open("genre_flags.txt", 'r+')
    flags_file_read = f.read()
    f.close()
    flag_file_input = flags_file_read.split(",")
    if genre_last_timestamp != flag_file_input[13]:  # Looking for change to time/date stamp.
        genre_last_timestamp = flag_file_input[13]
        f = open('genre_last_timestamp.txt', 'w')  # Reading timestamp.txt file
        f.write(flag_file_input[13])
        f.close()
        print "A new genre flags file has been detected."
        random_list = []


def mciSend(s):
    i = winmm.mciSendStringA(s, 0, 0, 0)
    if i != 0:
        print "Error %d in mciSendString %s" % (i, s)


def playMP3(mp3Name):
    mciSend("Close All")
    mciSend("Open \"%s\" Type MPEGVideo Alias theMP3" % mp3Name)
    mciSend("Play theMP3 Wait")
    mciSend("Close theMP3")


def flag_printer():
    print "flag_one = " + str(flag_one)
    print "flag_two = " + str(flag_two)
    print "flag_three = " + str(flag_three)
    print "flag_four = " + str(flag_four)
    print "flag_five = " + str(flag_five)
    print "flag_six = " + str(flag_six)
    print "flag_seven = " + str(flag_seven)
    print "flag_eight = " + str(flag_eight)
    print "flag_nine = " + str(flag_nine)
    print "flag_ten = " + str(flag_ten)
    print "flag_eleven = " + str(flag_eleven)
    print "flag_twelve = " + str(flag_twelve)
    print "flag_thirteen = " + str(flag_thirteen)
    print "flag_fourtenn = " + str(flag_fourteen)
    print "flag_fourteen_change = " + str(flag_fourteen_change)


def genre_only_random_sorter():
    genre_search_flag = []
    flag_one_remove_list = []
    flag_two_remove_list = []
    flag_three_remove_list = []
    flag_four_remove_list = []
    flag_five_remove_list = []
    remove_list = []  # clears remove_list in advance of use
    if flag_one != "":  # Creates genre_search_flag list from various flags
        genre_search_flag.append(flag_one)
    if flag_two != "":
        genre_search_flag.append(flag_two)
    if flag_three != "":
        genre_search_flag.append(flag_three)
    if flag_four != "":
        genre_search_flag.append(flag_four)
    if flag_five != "":
        genre_search_flag.append(flag_five)
    print "Genres to be searched are: " + str(genre_search_flag)  # Print to console.
    flag_number = 1  # Used to determine name of flag_xxx_remove_list
    for j in genre_search_flag:
        counter = 0
        for i in song_list:  # List created (remove_list) to be deleted from random_list based on Genre in flag_one.
            if j in song_list[counter][7]:  # Looks for same genre selection(flag_one) in song_list
                remove_list.append(counter)  # when matched adds song number to remove_list
            counter += 1
        for i in remove_list:  # This loop uses remove_list generated above to remove ongs from random_list
            counter = 0
            if i in random_list:
                random_list.remove(i)  # Removes song numbers from random_list
            counter += 1
            if flag_number == 1:  # assigns removed song numbers to appropriate remove list
                flag_one_remove_list = remove_list
            if flag_number == 2:  # assigns removed song numbers to appropriate remove list
                flag_two_remove_list = remove_list
            if flag_number == 3:  # assigns removed song numbers to appropriate remove list
                flag_three_remove_list = remove_list
            if flag_number == 4:  # assigns removed song numbers to appropriate remove list
                flag_four_remove_list = remove_list
            if flag_number == 5:  # assigns removed song numbers to appropriate remove list
                flag_five_remove_list = remove_list
        flag_number += 1
        remove_list = []  # clears remove_list so next Genre can use it during processing
    if flag_one != "":  # Combines and creates genre_remove_list
        genre_remove_list = flag_one_remove_list + flag_two_remove_list + flag_three_remove_list \
                            + flag_four_remove_list + flag_five_remove_list
    random.shuffle(random_list)
    random.shuffle(genre_remove_list)
    counter = -1
    for i in genre_remove_list:  # this loop places the removed songs at start of random_list in random order
        counter += 1
        song_insert = genre_remove_list[counter]
        random_list.insert(0, song_insert)


def multiple_year_random_sorter_no_genre():
    global flag_six  # Information on global variables at http://bit.ly/1Qx32aW.
    global flag_seven
    global random_list
    remove_list = random_list
    if flag_seven != "null":  # Code to create range of years.
        year_range = []
        x = int(flag_six)  # Integer conversion.
        for y in range(x, int(flag_seven) + 1):  # Code to generate year_range based on integer of flag_seven.
            year_range.append(x)  # Generation of year_range list.
            x += 1
        print "Year Range To Process: " + str(year_range)  # confirm year_range list once completed.
        year_remove_list = []  # list generated. Used to remove desired year based songs from remove_listist
        for i in year_range:
            for j in random_list_with_year:
                if str(i) == str(j[1]):
                    year_remove_list.append(j[0])
        # from remove_list so they can be placed at random_list front
        for i in year_remove_list:  # This loop removes the selected songs from remove_list
            remove_list.remove(i)  # Code to removes songs from remove_list
        random.shuffle(random_list)
        random.shuffle(year_remove_list)
        counter = -1
        for i in year_remove_list:  # this loop places removed songs at start of random_list in random order
            counter += 1
            song_insert = year_remove_list[counter]
            random_list.insert(0, song_insert)


def single_year_random_sorter_no_genre():

    global flag_six
    global random_list
    year_list_sorter = random_list_with_year
    year_range = flag_six
    print "Year To Process: " + str(year_range)  # Confirm to console year_range.
    year_remove_list = []  # List generated and later used to remove desired year based songs.
    i = len(year_list_sorter) - 1  # Code to create year_remove_list based on single year starts here.
    x = 0
    for j in range(0, i):
        if str(year_range) == year_list_sorter[x][1]:  # checks for year
            print "Match"
            year_remove_list.append(year_list_sorter[x][0])  # If year matched song number appended to year remove list.
        x += 1
    # Code to remove songs stored in year_remove_list from remove_list starts here
    for i in year_remove_list:  # Code to remove songs from remove_list to be placed at front of random_list.
        random_list.remove(i)  # Removes songs from remove_list.
    random.shuffle(random_list)
    random.shuffle(year_remove_list)
    counter = -1
    for i in year_remove_list:  # Loop places removed songs at start of random_list in random order
        counter += 1
        song_insert = year_remove_list[counter]
        random_list.insert(0, song_insert)


def genre_by_year_random_sorter():
    global flag_six  # Variables and lists to be accessed globally.
    global flag_seven
    global random_list
    genre_search_flag = []  # Variables used in function.
    flag_one_remove_list = []
    flag_two_remove_list = []
    flag_three_remove_list = []
    flag_four_remove_list = []
    flag_five_remove_list = []
    remove_list = []  # Clears remove_list in advance of use.
    if flag_one != "":  # Creates genre_search_flag list from various flags.
        genre_search_flag.append(flag_one)
    if flag_two != "":
        genre_search_flag.append(flag_two)
    if flag_three != "":
        genre_search_flag.append(flag_three)
    if flag_four != "":
        genre_search_flag.append(flag_four)
    if flag_five != "":
        genre_search_flag.append(flag_five)
    print "Genres to be searched are: " + str(genre_search_flag)  # Prints genres search  to console.
    flag_number = 1  # Used to determine name of flag_xxx_remove_list.
    for j in genre_search_flag:  # Loop creates various genre lists.
        print "Searching for"
        print j
        counter = 0
        for i in song_list:  # List created (remove_list) to be deleted from random_list based on Genre in flag_one.
            if j in song_list[counter][7]:  # Looks for same genre selection(flag_one) in song_list
                remove_list.append(counter)  # When matched adds song number to remove_list.
            counter += 1
        for i in remove_list:  # Uses remove_list to assign song numbers to lists and remove them from random_list.
            counter = 0
            if i in random_list:
                random_list.remove(i)  # Removes song number from random_list
            counter += 1
            if flag_number == 1:  # Assigns removed song numbers to appropriate remove list.
                flag_one_remove_list = remove_list
            if flag_number == 2:  # Assigns removed song numbers to appropriate remove list.
                flag_two_remove_list = remove_list
            if flag_number == 3:  # Assigns removed song numbers to appropriate remove list.
                flag_three_remove_list = remove_list
            if flag_number == 4:  # Assigns removed song numbers to appropriate remove list.
                flag_four_remove_list = remove_list
            if flag_number == 5:  # Assigns removed song numbers to appropriate remove list.
                flag_five_remove_list = remove_list
        flag_number += 1
        remove_list = []  # Clears remove_list so next Genre can use it during processing
    if flag_one != "":  # Combines and creates genre_remove_list
        genre_remove_list = flag_one_remove_list + flag_two_remove_list + flag_three_remove_list \
                            + flag_four_remove_list + flag_five_remove_list
        print "Full genre_remove_list: " + str(genre_remove_list)
    year_list_sorter = random_list_with_year  # random_list_with_year provides song number and year recorded in list.
    year_range = []
    if flag_seven == "null":  # Code for generating range of one year starts here
        year_range = flag_six
        print "Year To Process: " + str(year_range)  # Confirm to console year_range.
        year_remove_list = []  # List generated and later used to remove desired year based songs.
        i = len(year_list_sorter) - 1  # Code to create year_remove_list based on single year starts here.
        x = 0
        y = len(genre_remove_list)
        print"Looking for single year"
        print "Looking For " + str(year_range)
        for i in genre_remove_list:
            song_year_in_list = random_list_with_year[i][1]
            if song_year_in_list == str(year_range):
                year_remove_list.append(i)  # Adds to year_remove_list
        for i in year_remove_list:  # Loop uses year_remove_list generated above to remove songs from genre_remove_list.
                counter = 0
                if i in genre_remove_list:
                    genre_remove_list.remove(i)  # Removes song numbers from genre_remove_list.
                counter += 1
    else:  # Code for generating range of years starts here.
        print "Need To Process Year Range"  # Console message to confirm multi year range.
        x = int(flag_six)  # Start_year converted to integer.
        for y in range(x, int(flag_seven) + 1):  # Code to generate year_range based on flag_six and flag_seven.
            year_range.append(x)  # generation of year_range list
            x += 1
        print "Year Range To Process: " + str(year_range)  # Confirms year_range list to console.
        year_remove_list = []  # List generated. Used to remove desired year based songs from remove_list.
        for i in range(0, len(year_range)):
            x = 0
            for y in range(0, len(genre_remove_list)):  # Generates year_remove_list.
                if str(year_range[i]) == year_list_sorter[x][1]:  # Checks for year.
                    print "Match"
                    year_remove_list.append(year_list_sorter[x][0])  # Matched song number appended to year_remove_list.
                x += 1
        print str(len(year_remove_list)) + " songs to be remove_list so they can be placed at front of random_list."
        for i in year_remove_list:  # Uses year_remove_list to remove songs from genre_remove_list.
                counter = 0
                if i in genre_remove_list:
                    genre_remove_list.remove(i)  # Removes song numbers from genre_remove_list.
                counter += 1
    random.shuffle(random_list)  # List randomized.
    random.shuffle(genre_remove_list)  # List randomized.
    random.shuffle(year_remove_list)  # List randomized.
    counter = -1
    for i in genre_remove_list:  # Loop places removed songs at start of random_list in random order.
        counter += 1
        song_insert = genre_remove_list[counter]
        random_list.insert(0, song_insert)
    counter = -1
    random.shuffle(random_list)  # Randomizes returned non year genre songs with overall random_list.
    for i in year_remove_list:  # Removed songs in desired years placed at start of random_list in random order.
        counter += 1
        song_insert = year_remove_list[counter]
        random_list.insert(0, song_insert)


def artist_by_year_random_sorter():
    global flag_six  # Variables and lists to be accessed globally.
    global flag_seven
    global flag_eight
    global flag_nine
    global flag_ten
    global flag_eleven
    global flag_twelve
    global flag_thirteen
    global flag_fourteen
    global random_list
    artist_search_flag = []
    year_remove_list = []
    flag_eight_remove_list = []
    flag_nine_remove_list = []
    flag_ten_remove_list = []
    flag_eleven_remove_list = []
    flag_twelve_remove_list = []
    flag_thirteen_remove_list = []
    remove_list = []  # Clears remove_list in advance of use.
    if flag_eight != "":  # Creates genre_search_flag list from various flags.
        artist_search_flag.append(flag_eight)
    if flag_nine != "":
        artist_search_flag.append(flag_nine)
    if flag_ten != "":
        artist_search_flag.append(flag_ten)
    if flag_eleven != "":
        artist_search_flag.append(flag_eleven)
    if flag_twelve != "":
        artist_search_flag.append(flag_twelve)
    if flag_thirteen != "":
        artist_search_flag.append(flag_thirteen)
    print "Artists to be searched are: " + str(artist_search_flag)  # Prints artist search to console.
    flag_number = 1  # Used to determine name of flag_xxx_remove_list.
    for j in artist_search_flag:  # Loop creates various artist lists.
        print "Searching for"
        print j
        counter = 0
        for i in song_list:  # List created (remove_list) to be used later in deleting random_list songs.
            if j == song_list[counter][1]:  # Looks for same artist selection(flag_one) in song_list
                remove_list.append(counter)  # When matched adds song number to remove_list.
            counter += 1
        for i in remove_list:  # Uses remove_list to assign song numbers to lists and remove them from random_list.
            counter = 0
            if i in random_list:
                random_list.remove(i)  # Removes song number from random_list
            counter += 1
            if flag_number == 1:  # Assigns removed song numbers to appropriate remove list.
                flag_eight_remove_list = remove_list
            if flag_number == 2:  # Assigns removed song numbers to appropriate remove list.
                flag_nine_remove_list = remove_list
            if flag_number == 3:  # Assigns removed song numbers to appropriate remove list.
                flag_ten_remove_list = remove_list
            if flag_number == 4:  # Assigns removed song numbers to appropriate remove list.
                flag_eleven_remove_list = remove_list
            if flag_number == 5:  # Assigns removed song numbers to appropriate remove list.
                flag_twelve_remove_list = remove_list
            if flag_number == 6:  # Assigns removed song numbers to appropriate remove list.
                flag_thirteen_remove_list = remove_list
        flag_number += 1
        remove_list = []  # Clears remove_list so next Genre can use it during processing
        artist_remove_list = flag_eight_remove_list + flag_nine_remove_list + flag_ten_remove_list \
                             + flag_eleven_remove_list + flag_twelve_remove_list + flag_thirteen_remove_list
    year_list_sorter = random_list_with_year  # random_list_with_year provides song number and year recorded in list.
    year_range = []
    if flag_six != "null" and flag_seven == "null":  # Code for generating range of one year starts here
        year_range = flag_six
        print "Year To Process: " + str(year_range)  # Confirm to console year_range.
        year_remove_list = []  # List generated and later used to remove desired year based songs.
        i = len(year_list_sorter) - 1  # Code to create year_remove_list based on single year starts here.
        x = 0
        y = len(artist_remove_list)
        print"Looking for single year"
        print "Looking For " + str(year_range)
        for i in artist_remove_list:
            song_year_in_list = random_list_with_year[i][1]
            if song_year_in_list == str(year_range):
                year_remove_list.append(i)  # Adds to year_remove_list
        for i in year_remove_list:  # Loop uses year_remove_list to remove songs from artist_remove_list.
                counter = 0
                if i in artist_remove_list:
                    artist_remove_list.remove(i)  # Removes song numbers from artist_remove_list.
                counter += 1
    if flag_six != "null" and flag_seven != "null":  # Code for generating range of years starts here.
        print "Need To Process Year Range"  # Console message to confirm multi year range.
        x = int(flag_six)  # Start_year converted to integer.
        for y in range(x, int(flag_seven) + 1):  # Code to generate year_range based on flag_six and flag_seven.
            year_range.append(x)  # generation of year_range list
            x += 1
        print "Year Range To Process: " + str(year_range)  # Confirms year_range list to console.
        year_remove_list = []  # List generated. Used to remove desired year based songs from remove_list.
        for i in range(0, len(year_range)):
            x = 0
            for y in range(0, len(artist_remove_list)):  # Generates year_remove_list.
                if str(year_range[i]) == year_list_sorter[x][1]:  # Checks for year.
                    year_remove_list.append(year_list_sorter[x][0])  # If matched song number appended to
                x += 1
        print str(len(year_remove_list)) + " songs to be remove_list so they can be placed at front of random_list."
        for i in year_remove_list:  # Uses year_remove_list to remove songs from genre_remove_list.
                counter = 0
                if i in artist_remove_list:
                    artist_remove_list.remove(i)  # Removes song numbers from genre_remove_list.
                counter += 1
    random.shuffle(random_list)  # List randomized.
    random.shuffle(artist_remove_list)  # List randomized.
    random.shuffle(year_remove_list)  # List randomized.
    counter = -1
    for i in artist_remove_list:  # Loop places removed songs at start of random_list in random order.
        counter += 1
        song_insert = artist_remove_list[counter]
        random_list.insert(0, song_insert)
    if flag_six != "null":
        random.shuffle(random_list)  # Randomizes returned non year artist songs with overall random_list.
    counter = -1
    for i in year_remove_list:  # Removed songs in desired years placed at start of random_list in random order.
        counter += 1
        song_insert = year_remove_list[counter]
        random_list.insert(0, song_insert)


def genre_year_artist_random_sort_engine():
    if flag_one != "none" and flag_six == "null" and flag_seven == "null" and flag_eight == "null" \
            and flag_nine == "null" and flag_ten == "null" and flag_eleven == "null" and flag_twelve == "null" \
            and flag_thirteen == "null":
        genre_only_random_sorter()
    if flag_one == "none" and flag_six != "null" and flag_seven != "null" and flag_eight == "null" \
            and flag_nine == "null" and flag_ten == "null" and flag_eleven == "null" and flag_twelve == "null" \
            and flag_thirteen == "null":
        multiple_year_random_sorter_no_genre()
    if flag_one == "none" and flag_six != "null" and flag_seven == "null" and flag_eight == "null" \
            and flag_nine == "null" and flag_ten == "null" and flag_eleven == "null" and flag_twelve == "null" \
            and flag_thirteen == "null":
        single_year_random_sorter_no_genre()
    if flag_one != "none" and flag_six != "null" and flag_eight == "null" and flag_nine == "null" \
            and flag_ten == "null" and flag_eleven == "null" and flag_twelve == "null" and flag_thirteen == "null":
        genre_by_year_random_sorter()
    if flag_one == "none":
        if flag_eight != "null" or flag_nine != "null" or flag_ten != "null" or flag_eleven != "null" \
                or flag_twelve != "null" or flag_thirteen != "null":
            artist_by_year_random_sorter()

def artist_list_generator():
    artist_list =[]
    x=0
    for i in song_list:
        if song_list[x][1] not in artist_list:
            artist_list.append(song_list[x][1])
        x +=1
    print artist_list
    artist_list_file_populate = open('artist_list.pkl', 'wb')
    pickle.dump(artist_list, artist_list_file_populate)
    artist_list_file_populate.close()
    print "artist_list.pkl populated."

set_up_user_files_first_time()
write_jukebox_startup_to_log()  # Writes Jukebox start time to log.
genre_read_and_select_engine()  # Invokes and builds lists for random play genre selection process.
count_number_mp3_songs()  # Counts number of .mp3 files in /music.
if not song_list:
    song_list_generator()
artist_list_generator()
infinite_loop = 1  # Jukebox infinite loop.
while infinite_loop == 1:  # This infinite loop is the mp3 playback engine for the Jukebox. http://bit.ly/1vHqVkJ
    play_list_loader()  # Loads paid play_list
    if len(play_list) > 0:  # Checks for any paid songs to play
        play_list_player()  # Plays paid songs
    genre_read_and_select_engine()
    genre_file_change_detector()  # Looks for change to genre_flags.txt If file changed deletes existing random_list.
    if len(random_list) > 0:  # Plays random song.
        print "Proceeding to bottom of sequence."
    if not random_list:  # This code sets up random_list and random_list_with_year for all routines to use
        basic_random_list_generator()
        flag_printer()
        genre_year_artist_random_sort_engine()
    norandom_song_number_test = random_list[0]  # Test for norandom song designation.
    if "norandom" in str(song_list[norandom_song_number_test][7]):
        print song_list[norandom_song_number_test][7]
        del random_list[0]  # Deletes norandom song before playback.
    x = random_list[0]
    title = str(song_list[x][0])
    artist = str(song_list[x][1])
    album = str(song_list[x][2])
    year = (song_list[x][3])
    time = (song_list[x][6])
    random_mode_playback()
    if random_change_list == "yes":
        random_list = []
