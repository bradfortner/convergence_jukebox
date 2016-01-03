# Convergence Jukebox is Python based codes that emulates a Jukebox and plays mp3 media.
# Copyright (C) 2012 by Brad Fortner
# This program is free software you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation;
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program.
# If not, see http://www.gnu.org/licenses.
# The authour, information on, executable downloads and source code can be obtained via www.convergencejukebox.com

# Convergence Jukebox employs the hsaudiotag Python library which is released under an OSI BSD licence.
# hsaudiotag see: https://pypi.python.org/pypi/hsaudiotag
# Convergence Jukebox employs the playmp3.py Python library for windows Copyright (c) 2011 by James K. Lawless
# playmp3.py has been released under an MIT / X11 licence. See: http://www.mailsend-online.com/license.php.
# Convergence Jukebox employs the PyRSS2Gen Python Library.
# PyRSS2Gen is copyright (c) by Andrew Dalke Scientific, AB (previously
# Dalke Scientific Software, LLC) and is released under the BSD license.
# Info on PyRSS2Gen at http://www.dalkescientific.com/Python/PyRSS2Gen.html

import pickle  # Used to save and reload python lists.
import tkFont
import Tkinter as tk
from PIL import Image, ImageTk
from operator import itemgetter
import datetime  # Used in RSS generation.
import PyRSS2Gen  # Used n RSS generation.
import getpass  # Gets user name http://stackoverflow.com/questions/4325416/how-do-i-get-the-username-in-python.
import os
import os.path, time
import sys  # Used to check and switch resolutions for convergence jukebox.
from ctypes import *  # Used by playmp3.py windows based mp3 player.
# http://www.mailsend-online.com/blog/play-mp3-files-with-python-on-windows.html

computer_account_user_name = getpass.getuser()  # Used to write various log and RSS files to local directories.
winmm = windll.winmm  # Variable used in playmp3.py.
full_path = os.path.realpath('__file__')  # http://bit.ly/1RQBZYF

def mciSend(s):  # Function of playmp3.py
    i = winmm.mciSendStringA(s, 0, 0, 0)
    if i != 0:
        print "Error %d in mciSendString %s" % (i, s)


def playMP3(mp3Name):  # Function of playmp3.py
    mciSend("Close All")
    mciSend("Open \"%s\" Type MPEGVideo Alias theMP3" % mp3Name)
    mciSend("Play theMP3 Wait")
    mciSend("Close theMP3")


def side_info_display(event=None):

    display_info_recover = open("output_list.txt", 'r+')
    output_list_read = display_info_recover.read()
    display_info_recover.close()
    display_info = output_list_read.split(",")

    global side_line01, side_line02, side_line03, side_line04, side_line05, side_line06, side_line11, side_line12
    global side_line13, side_line14, side_line15, side_line17, side_line16, side_line18, side_line19, side_line20
    global side_line21, side_line22, side_line23, side_line24, side_line25, side_line26, side_line27, side_line28
    global side_line29, side_line30, side_line31, side_line32  # side_line variables found on side display from top.
    global sort_mode
    upcoming1 = upcoming2 = upcoming3 = upcoming4 = upcoming5 = upcoming6 = upcoming7 = upcoming8 = upcoming9 = ""
    upcoming10 = upcoming11 = upcoming12 = upcoming13 = upcoming14 = upcoming15 = upcoming16 = upcoming17 = ""
    upcoming18 = ""
    song_play_mode = song_play_mode1 = song_play_mode2 = song_play_mode3 = song_play_mode4 = song_play_mode5 = ""
    song_play_mode6 = song_play_mode7 = song_play_mode8 = song_play_mode9 = song_play_mode10 = ""

    # Title Artist Sort At Top Of Display

    side_line06 = tk.Label(panel1, text=sort_mode, font="Helvetica 28", background="#161e15", foreground="#81ab49",
                           anchor="nw")
    side_line06.pack()
    side_line06.place(x=45, y=61)

    # Random/Selection second line on screen
    song_play_mode = display_info[5]
    side_line01 = tk.Label(panel1, text=song_play_mode, font="Helvetica 12", background="#161e15", foreground="#81ab49",
                           anchor="nw")
    side_line01.pack()
    side_line01.place(x=40, y=111)

    # Song Title 3rd line on screen
    song_play_mode1 = "Title: " + display_info[0]
    side_line02 = tk.Label(panel1, text=song_play_mode1, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line02.pack()
    side_line02.place(x=40, y=131)

    # Song Artist 4th line on screen
    song_play_mode2 = "Artist: " + display_info[1]
    side_line03 = tk.Label(panel1, text=song_play_mode2, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line03.pack()
    side_line03.place(x=40, y=151)

    # Release Year/Length 5th line on screen
    song_play_mode3 = "Year: " + str(display_info[3]) + "   Length: " + display_info[4]
    side_line04 = tk.Label(panel1, text=song_play_mode3, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line04.pack()
    side_line04.place(x=40, y=171)

    # Album Title 6th line on screen
    song_play_mode4 = "Album: " + display_info[2]
    side_line05 = tk.Label(panel1, text=song_play_mode4, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line05.pack()
    side_line05.place(x=40, y=191)

    # Upcoming Selections 7th line on screen
    side_line11 = tk.Label(panel1, text="UPCOMING SELECTIONS", font="Helvetica 19", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line11.pack()
    side_line11.place(x=45, y=221)

    # upcoming_list_recover = open('c:/media/data/upcoming_list.pkl', 'rb')
    upcoming_list_recover = open('upcoming_list.pkl', 'rb')
    upcoming_list = pickle.load(upcoming_list_recover)
    upcoming_list_recover.close()
    del upcoming_list_recover

    # Upcoming selection 1.
    if len(upcoming_list) > 0:
        upcoming1 = upcoming_list[0]
    side_line12 = tk.Label(panel1, text=upcoming1, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line12.pack()
    side_line12.place(x=40, y=256)

    # Upcoming selection 2.
    if len(upcoming_list) > 1:
        upcoming2 = upcoming_list[1]
    side_line13 = tk.Label(panel1, text=upcoming2, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line13.pack()
    side_line13.place(x=40, y=273)

    # Upcoming selection 3.
    if len(upcoming_list) > 2:
        upcoming3 = upcoming_list[2]
    side_line14 = tk.Label(panel1, text=upcoming3, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line14.pack()
    side_line14.place(x=40, y=290)

    # Upcoming selection 4.
    if len(upcoming_list) > 3:
        upcoming4 = upcoming_list[3]
    side_line15 = tk.Label(panel1, text=upcoming4, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line15.pack()
    side_line15.place(x=40, y=307)

    # Upcoming selection 5.
    if len(upcoming_list) > 4:
        upcoming5 = upcoming_list[4]
    side_line16 = tk.Label(panel1, text=upcoming5, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line16.pack()
    side_line16.place(x=40, y=324)

    # Upcoming selection 6.
    if len(upcoming_list) > 5:
        upcoming6 = upcoming_list[5]
    side_line17 = tk.Label(panel1, text=upcoming6, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line17.pack()
    side_line17.place(x=40, y=341)

    # Upcoming selection 7.
    if len(upcoming_list) > 6:
        upcoming7 = upcoming_list[6]
    side_line18 = tk.Label(panel1, text=upcoming7, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line18.pack()
    side_line18.place(x=40, y=358)

    # Upcoming selection 8.
    if len(upcoming_list) > 7:
        upcoming8 = upcoming_list[7]
    side_line19 = tk.Label(panel1, text=upcoming8, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line19.pack()
    side_line19.place(x=40, y=375)

    # Upcoming selection 9.
    if len(upcoming_list) > 8:
        upcoming9 = upcoming_list[8]
    side_line20 = tk.Label(panel1, text=upcoming9, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line20.pack()
    side_line20.place(x=40, y=392)

    # Upcoming selection 10.
    if len(upcoming_list) > 9:
        upcoming10 = upcoming_list[9]
    side_line21 = tk.Label(panel1, text=upcoming10, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line21.pack()
    side_line21.place(x=40, y=409)

    # Upcoming selection 11.
    if len(upcoming_list) > 10:
        upcoming11 = upcoming_list[10]
    side_line25 = tk.Label(panel1, text=upcoming11, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line25.pack()
    side_line25.place(x=40, y=426)

    # Upcoming selection 12.
    if len(upcoming_list) > 11:
        upcoming12 = upcoming_list[11]
    side_line26 = tk.Label(panel1, text=upcoming12, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line26.pack()
    side_line26.place(x=40, y=443)

    # Upcoming selection 13.
    if len(upcoming_list) > 12:
        upcoming13 = upcoming_list[12]
    side_line27 = tk.Label(panel1, text=upcoming13, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line27.pack()
    side_line27.place(x=40, y=460)

    # Upcoming selection 14.
    if len(upcoming_list) > 13:
        upcoming14 = upcoming_list[13]
    side_line28 = tk.Label(panel1, text=upcoming14, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line28.pack()
    side_line28.place(x=40, y=477)

    # Upcoming selection 15.
    if len(upcoming_list) > 14:
        upcoming15 = upcoming_list[14]
    side_line29 = tk.Label(panel1, text=upcoming15, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line29.pack()
    side_line29.place(x=40, y=494)

    # Upcoming selection 16.
    if len(upcoming_list) > 15:
        upcoming16 = upcoming_list[15]
    side_line30 = tk.Label(panel1, text=upcoming16, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line30.pack()
    side_line30.place(x=40, y=511)

    # Upcoming selection 17.
    if len(upcoming_list) > 16:
        upcoming17 = upcoming_list[16]
    side_line31 = tk.Label(panel1, text=upcoming17, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line31.pack()
    side_line31.place(x=40, y=528)

    # Upcoming selection 18.
    if len(upcoming_list) > 17:
        upcoming18 = upcoming_list[17]
    side_line32 = tk.Label(panel1, text=upcoming18, background="#161e15", foreground="#81ab49", anchor="nw")
    side_line32.pack()
    side_line32.place(x=40, y=545)

    # Credits indicator.
    side_line23 = tk.Label(panel1, text="CREDITS " + str(credit_amount), font="Helvetica 28", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line23.pack()
    side_line23.place(x=98, y=566)

    # Payment barker line.
    side_line22 = tk.Label(panel1, text="Twenty-Five Cents Per Selection", font="Helvetica 14", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line22.pack()
    side_line22.place(x=62, y=606)

    song_total = len(song_list)
    # Selections available line.
    side_line24 = tk.Label(panel1, text=str(song_total) + " Song Selections Available", font="Helvetica 14",
                           background="#161e15", foreground="#81ab49", anchor="nw")
    side_line24.pack()
    side_line24.place(x=65, y=627)


def screen_display(event=None):  # Function assigns songs and places the 16 buttons placed on the screen.
    # song_list is used to build final list of all songs including ID3 information and file location. song_list
    # information locations: songTitle = song_list[x][0], songArtist = song_list[x][1], songAlbum = song_list[x][2],
    # songYear = song_list[x][3], songDurationSeconds = song_list[x][4], songGenre = song_list[x][5],
    # songDurationTime = song_list[x][6], songComment = song_list[x][7]
    # Title = song_list[x][0], songArtist = song_list[x][1].
    global song0, song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14
    global song15, screen_number, modulus, font_type, song_artist_label, first_pass
    global sn0, sn1, sn2, sn3, sn4, sn5, sn6, sn7, sn8, sn9, sn10, sn11, sn12, sn13, sn14, sn15  # For whichsong_number.
    global cursor_position  # This routine sets cursor_position as global bringing in variable outside of function

    if first_pass == 1:  # this routine fixes first pass garbage collection problem when jukebox left on first screen
        first_pass += 1
    else:
        button_destroyer()

    song_artist_label = screen_number * 16

    side_info_display()  # Updates side window.

    current_song_display_updater()  # This function writes the now playing information to the top of the screen.

    # Following lines of code put song selection buttons on the screen panel.

    sn0 = song_list[song_artist_label][9]
    font_size()
    song0 = tk.Button(panel1, highlightcolor="Red", highlightthickness=20, font=str(font_type),
                      command=lambda: song_entry(sn0), background="black", foreground="white",
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song0.pack()
    song0.place(x=491, y=227, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn1 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song1 = tk.Button(panel1, font=str(font_type), command=lambda: song_entry(sn1), background="black",
                      foreground="white", text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song1.pack()
    song1.place(x=491, y=281, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn2 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song2 = tk.Button(panel1, font=str(font_type), command=lambda: song_entry(sn2), background="black",
                      foreground="white", text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song2.pack()
    song2.place(x=491, y=335, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn3 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song3 = tk.Button(panel1, command=lambda: song_entry(sn3), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song3.pack()
    song3.place(x=491, y=389, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn4 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song4 = tk.Button(panel1, command=lambda: song_entry(sn4), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song4.pack()
    song4.place(x=491, y=443, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn5 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song5 = tk.Button(panel1, command=lambda i=sn5: song_entry(i), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song5.pack()
    song5.place(x=491, y=497, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn6 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song6 = tk.Button(panel1, command=lambda: song_entry(sn6), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song6.pack()
    song6.place(x=491, y=551, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn7 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song7 = tk.Button(panel1, command=lambda: song_entry(sn7), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song7.pack()
    song7.place(x=491, y=605, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn8 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song8 = tk.Button(panel1, command=lambda: song_entry(sn8), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song8.pack()
    song8.place(x=833, y=227, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn9 = song_list[song_artist_label][9]
    font_size()
    song9 = tk.Button(panel1, command=lambda: song_entry(sn9), background="black", foreground="white",
                      font=str(font_type),
                      text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song9.pack()
    song9.place(x=833, y=281, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn10 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song10 = tk.Button(panel1, command=lambda: song_entry(sn10), background="black", foreground="white",
                       font=str(font_type),
                       text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song10.pack()
    song10.place(x=833, y=335, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn11 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song11 = tk.Button(panel1, command=lambda: song_entry(sn11), background="black", foreground="white",
                       font=str(font_type),
                       text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song11.pack()
    song11.place(x=833, y=389, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn12 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song12 = tk.Button(panel1, command=lambda: song_entry(sn12), background="black", foreground="white",
                       font=str(font_type),
                       text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song12.pack()
    song12.place(x=833, y=443, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn13 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song13 = tk.Button(panel1, command=lambda: song_entry(sn13), background="black", foreground="white",
                       font=str(font_type),
                       text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song13.pack()
    song13.place(x=833, y=497, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn14 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song14 = tk.Button(panel1, command=lambda: song_entry(sn14), background="black", foreground="white",
                       font=str(font_type),
                       text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song14.pack()
    song14.place(x=833, y=551, width=335, height=50)  # Place attribute positions button using x,y variables.

    song_artist_label += 1
    sn15 = song_list[song_artist_label][9]
    font_type = ""  # Garbage collection.
    font_size()
    song15 = tk.Button(panel1, command=lambda: song_entry(sn15), background="black", foreground="white",
                       font=str(font_type),
                       text=song_list[song_artist_label][0] + "\n" + song_list[song_artist_label][1])
    song15.pack()
    song15.place(x=833, y=605, width=335, height=50)  # Place attribute positions button using x,y variables.

    font_type = ""  # Garbage collection.
    song_artist_label = ""
    screen_button()  # This function call is required to focus the appropriate song button.


def current_song_display_updater(event=None):  # Updates the song playing information at the top of the screen.
    global text_display_1, jukebox_info_display_1, jukebox_info_display_2, jukebox_name
    display_info_recover = open("output_list.txt", 'r+')
    output_list_read = display_info_recover.read()
    display_info_recover.close()
    display_info = output_list_read.split(",")
    text_display_1 = display_info[0]
    text_display_2 = display_info[1]

    # Writes the jukebox name at top centre of screen
    jukebox_name = tk.Button(panel1, bd=0, disabledforeground="black", background="white", foreground="black",
                             font="Helvetica 28 bold", text='Convergence Music System')
    jukebox_name.pack()
    jukebox_name.place(x=576, y=39, width=500, height=50)
    jukebox_name.config(state='disabled')

    # Actve Song Title
    if len(text_display_1) > 47:  # Statement changes size of song title fonts depending upon number of characters.
        jukebox_info_display_1 = tk.Button(panel1, text=str(text_display_1), bd=0, font="Helvetica 13",
                                           disabledforeground="white", background="black", foreground="white")
    elif len(text_display_1) < 35:
        jukebox_info_display_1 = tk.Button(panel1, text=str(text_display_1), bd=0, font="Helvetica 28",
                                           disabledforeground="white", background="black", foreground="white")
    else:
        jukebox_info_display_1 = tk.Button(panel1, text=str(text_display_1), bd=0, font="Helvetica 18",
                                           disabledforeground="white", background="black", foreground="white")
    jukebox_info_display_1.pack()
    jukebox_info_display_1.place(x=528, y=113, width=600, height=40)  # Place attribute positions button using
    # x,y variables., size of button with width and height.
    jukebox_info_display_1.config(state='disabled')

    #  Active Artist/Title.
    if len(
            text_display_2) < 30:  # Statement changes size of song artist fonts depending upon number of characters.
        jukebox_info_display_2 = tk.Button(panel1, text=str(text_display_2), bd=0, font="Helvetica 28",
                                           disabledforeground="white", background="black", foreground="white")
    else:
        jukebox_info_display_2 = tk.Button(panel1, text=str(text_display_2), bd=0, font="Helvetica 18", anchor='n',
                                           disabledforeground="white", background="black", foreground="white")
    jukebox_info_display_2.pack()
    jukebox_info_display_2.place(x=492, y=160, width=670, height=40)  # Place attribute positions button using
    # x,y variables., size of button with width and height.
    jukebox_info_display_2.config(state='disabled')
    text_display_2 = ""


def song_entry(song_number):  # This function writes selected song to playlist.

    global credit_amount
    if credit_amount == 0:
        playMP3('buzz.mp3')
        clear_alpha_keys()
        return
    play_list_recover = open('play_list.pkl', 'rb')
    play_list = pickle.load(play_list_recover)
    play_list_recover.close()
    new_entry = song_number
    print new_entry
    # Check to see if duplicate entry on play_list goes here
    if new_entry in play_list:  # Checks to see if song number is in play_list
        a = play_list.index(song_number)  # Locates song number in play_list. Index number assigned to variable.
        # http://stackoverflow.com/questions/7571635/python-fastest-way-to-check-if-a-value-exist-in-a-array
        b = play_list[a]  # b variable assigned song number at play_list index provided in above line.
        if song_number == b:
            return
    # Check to see if duplicate entry on play_list ends here
    x = 0
    while x < len(song_list):  # Saves all upcoming song titles and artist to upcoming_list for side display.
        if song_list[x][9] == new_entry:
            print song_list[x][0]
            upcoming_song = str(song_list[x][0]) + " - " + str(song_list[x][1])
            # upcoming_list_recover = open('c:/media/data/upcoming_list.pkl', 'rb')
            upcoming_list_recover = open('upcoming_list.pkl', 'rb')
            upcoming_list = pickle.load(upcoming_list_recover)
            upcoming_list_recover.close()
            upcoming_list.append(upcoming_song)
            # upcoming_list_save = open('c:/media/data/upcoming_list.pkl', 'wb')
            upcoming_list_save = open('upcoming_list.pkl', 'wb')
            pickle.dump(upcoming_list, upcoming_list_save)
            upcoming_list_save.close()
        x += 1

    play_list.append(new_entry)
    play_list_save = open('play_list.pkl', 'wb')
    pickle.dump(play_list, play_list_save)
    play_list_save.close()
    credit_amount -= 1
    playMP3('success.mp3')
    screen_caller_down()


def credit_calculator(event=None):
    global credit_amount
    credit_amount += 1
    print credit_amount
    screen_caller_down()


def year_sort(event=None):  # This function sorts the song_list by year. Feature not implemented.
    global sort_mode
    sort_mode = ""
    sort_mode = "Sort Mode By Year"
    song_list.sort(key=itemgetter(3), reverse=False)
    screen_caller_down()


def title_sort(event=None):  # This function sorts the song_list by title.
    global sort_mode
    global which_song_number  # Used by artistSort() and title_sort().
    global cursor_position  # This routine sets cursor_position as global bringing in variable outside of function.
    global screen_number
    global modulus
    sort_mode = ""
    sort_mode = "Sort Mode By Title"
    song_list.sort(key=itemgetter(0), reverse=False)
    a = 0
    while a < len(song_list):  # Ensures selection display stays on same song when switch between Artist and Title sort.
        if song_list[a][9] == which_song_number:
            cursor_position = a
            print cursor_position
            screen_number = cursor_position / 16
            remainder = cursor_position % 16
            if screen_number == 0:
                modulus = remainder - 1
            else:
                modulus = remainder
            screen_display()
            return
        a += 1
    screen_caller_down()


def artist_sort(event=None):  # This function sorts the song_list by artist.
    global sort_mode
    global which_song_number  # Used by artist_sort() and title_sort().
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    sort_mode = ""
    sort_mode = "Sort Mode By Artist"
    song_list.sort(key=itemgetter(1), reverse=False)
    a = 0
    while a < len(song_list):  # Ensures selection display stays on same song when switch between Artist and Title sort.
        if song_list[a][9] == which_song_number:
            cursor_position = a
            print cursor_position
            screen_number = cursor_position / 16
            remainder = cursor_position % 16
            if screen_number == 0:
                modulus = remainder - 1
            else:
                modulus = remainder
            screen_display()
            return
        a += 1
    screen_caller_down()


def font_size(event=None):  # This routine scales button font size depending upon length of title/artist.
    global font_type
    global song_artist_label

    y = len(song_list[song_artist_label][0])
    z = len(song_list[song_artist_label][1])

    if y >= z:  # Compares length of title and length of artist to determine larger argument for font_size selection.
        x = y
    else:
        x = z
    if x >= 50:
        font_type = tkFont.Font(family="Helvetica", size=8, weight="bold")
    elif x == 49:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 48:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 47:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 46:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 45:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 44:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 43:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 42:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 41:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 40:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 39:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 38:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    elif x == 37:
        font_type = tkFont.Font(family="Helvetica", size=9, weight="bold")
    else:
        font_type = tkFont.Font(family="Helvetica", size=11, weight="bold")
    del x
    del y


def button_destroyer(event=None):  # Used to stop button memory leak.
    song0.destroy()
    song1.destroy()
    song2.destroy()
    song3.destroy()
    song4.destroy()
    song5.destroy()
    song6.destroy()
    song7.destroy()
    song8.destroy()
    song9.destroy()
    song10.destroy()
    song11.destroy()
    song12.destroy()
    song13.destroy()
    song14.destroy()
    song15.destroy()

    jukebox_name.destroy()
    jukebox_info_display_1.destroy()
    jukebox_info_display_2.destroy()

    side_line01.destroy()
    side_line02.destroy()
    side_line03.destroy()
    side_line04.destroy()
    side_line05.destroy()
    side_line06.destroy()
    side_line11.destroy()
    side_line12.destroy()
    side_line13.destroy()
    side_line14.destroy()
    side_line15.destroy()
    side_line16.destroy()
    side_line17.destroy()
    side_line18.destroy()
    side_line19.destroy()
    side_line20.destroy()
    side_line21.destroy()
    side_line22.destroy()
    side_line23.destroy()
    side_line24.destroy()
    side_line25.destroy()
    side_line26.destroy()
    side_line27.destroy()
    side_line28.destroy()
    side_line29.destroy()
    side_line30.destroy()
    side_line31.destroy()
    side_line32.destroy()


def screen_button(event=None):  # This function focuses buttons based on modulus value
    global modulus
    global sn0, sn1, sn2, sn3, sn4, sn5, sn6, sn7, sn8, sn9, sn10, sn11, sn12, sn13, sn14, sn15
    global which_song_number  # Used by artist_sort() and title_sort()

    # Returns all buttons to black background.

    song0.configure(background='black')
    song1.configure(background='black')
    song2.configure(background='black')
    song3.configure(background='black')
    song4.configure(background='black')
    song5.configure(background='black')
    song6.configure(background='black')
    song7.configure(background='black')
    song8.configure(background='black')
    song9.configure(background='black')
    song10.configure(background='black')
    song11.configure(background='black')
    song12.configure(background='black')
    song13.configure(background='black')
    song14.configure(background='black')
    song15.configure(background='black')

    if modulus <= 0:
        song0.focus_set()
        song0.configure(background="#3b3b3b")
        which_song_number = sn0
        if modulus < 0:
            modulus = 0
    elif modulus == 1:
        song1.focus_set()
        song1.configure(background="#3b3b3b")
        which_song_number = sn1
    elif modulus == 2:
        song2.focus_set()
        song2.configure(background="#3b3b3b")
        which_song_number = sn2
    elif modulus == 3:
        song3.focus_set()
        song3.configure(background="#3b3b3b")
        which_song_number = sn3
    elif modulus == 4:
        song4.focus_set()
        song4.configure(background="#3b3b3b")
        which_song_number = sn4
    elif modulus == 5:
        song5.focus_set()
        song5.configure(background="#3b3b3b")
        which_song_number = sn5
    elif modulus == 6:
        song6.focus_set()
        song6.configure(background="#3b3b3b")
        which_song_number = sn6
    elif modulus == 7:
        song7.focus_set()
        song7.configure(background="#3b3b3b")
        which_song_number = sn7
    elif modulus == 8:
        song8.focus_set()
        song8.configure(background="#3b3b3b")
        which_song_number = sn8
    elif modulus == 9:
        song9.focus_set()
        song9.configure(background="#3b3b3b")
        which_song_number = sn9
    elif modulus == 10:
        song10.focus_set()
        song10.configure(background="#3b3b3b")
        which_song_number = sn10
    elif modulus == 11:
        song11.focus_set()
        song11.configure(background="#3b3b3b")
        which_song_number = sn11
    elif modulus == 12:
        song12.focus_set()
        song12.configure(background="#3b3b3b")
        which_song_number = sn12
    elif modulus == 13:
        song13.focus_set()
        song13.configure(background="#3b3b3b")
        which_song_number = sn13
    elif modulus == 14:
        song14.focus_set()
        song14.configure(background="#3b3b3b")
        which_song_number = sn14
    elif modulus == 15:
        song15.focus_set()
        song15.configure(background="#3b3b3b")
        which_song_number = sn15
    print "which_song_number at screen_button :" + str(which_song_number)


def down(event=None):  # This function defines actions taken when the down arrow key is pressed.
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global modulus
    global song_list
    global screen_number
    global last_screen
    b = len(song_list)
    if cursor_position == b:
        return
    else:
        cursor_position += 1
        modulus += 1
        if modulus < 0:
            screen_caller_up()
        if modulus > 15:
            screen_caller_down()
    screen_button()


def right(event=None):  # This function defines actions taken when the right arrow key is pressed.
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global modulus
    b = len(song_list)
    b -= 8
    if cursor_position >= b:
        return
    cursor_position += 8
    modulus += 8
    if modulus < 0:
        screen_caller_up()
    if modulus > 15:
        screen_caller_down()
    screen_button()
    b = len(song_list)


def screen_caller_down(event=None):  # This function defines appropriate screens as the user moves down the song_list.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    screen_number = cursor_position / 16
    remainder = cursor_position % 16
    if screen_number == 0:
        modulus = remainder - 1
    else:
        modulus = remainder
    screen_display()


def screen_caller_up(event=None):  # This function defines appropriate screens as the user moves up the song_list.
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    screen_number = cursor_position / 16
    modulus = cursor_position % 16
    screen_display()


def up(event=None):  # This function defines actions taken when the up arrow key is pressed.
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global modulus
    global screen_number
    cursor_position -= 1
    modulus -= 1
    if screen_number == 0:  # Trap so user can't go past 0 going backwards.
        if modulus < 0:
            modulus = 0
            cursor_position = 0
    if modulus < 0:
        screen_caller_up()
    if modulus > 15:
        screen_caller_down()
    screen_button()


def left(event=None):  # This function defines actions taken when the left arrow key is pressed.
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global modulus
    global screen_number
    cursor_position -= 8
    modulus -= 8
    if screen_number == 0:  # Trap so user can't go past 0 going backwards.
        if modulus < 0:
            modulus = 0
            cursor_position = 0
    if modulus < 0:
        screen_caller_up()
    if modulus > 15:
        screen_caller_down()
    screen_button()


def clear_alpha_keys(event=None):
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter..
    d_key_press = 0
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    w_key_press = 0
    t_key_press = 0


def alphabet_sort_jump_a(event=None):  # This function defines the first title for each letter..
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    d_key_press = 0  # Resets other multikeys to base letter..
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    t_key_press = 0
    w_key_press = 0
    a_key_press += 1
    if a_key_press == 4:
        a_key_press = 1
    if a_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "A":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "A":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if a_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "B":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "B":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if a_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "C":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "C":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_d(event=None):  # This function defines the first title for each letter..
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    t_key_press = 0
    w_key_press = 0
    d_key_press += 1
    if d_key_press == 4:
        d_key_press = 1
    if d_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "D":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "D":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if d_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "E":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "E":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if d_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "F":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "F":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_g(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    d_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    t_key_press = 0
    w_key_press = 0
    g_key_press += 1
    if g_key_press == 4:
        g_key_press = 1
    if g_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "G":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "G":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if g_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "H":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "H":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if g_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "I":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "I":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_j(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    d_key_press = 0
    g_key_press = 0
    m_key_press = 0
    p_key_press = 0
    t_key_press = 0
    w_key_press = 0
    j_key_press += 1
    if j_key_press == 4:
        j_key_press = 1
    if j_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "J":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "J":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if j_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "K":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "K":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if j_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "L":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "L":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_m(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    d_key_press = 0
    g_key_press = 0
    j_key_press = 0
    p_key_press = 0
    t_key_press = 0
    w_key_press = 0
    m_key_press += 1
    if m_key_press == 4:
        m_key_press = 1
    if m_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "M":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "M":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if m_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "N":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "N":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if m_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "O":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "O":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_p(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    d_key_press = 0
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    t_key_press = 0
    w_key_press = 0
    p_key_press += 1
    if p_key_press == 4:
        p_key_press = 1
    if p_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "P":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "P":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if p_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "Q":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "Q":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if p_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "R":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "R":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_s(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    clear_alpha_keys()

    if sort_mode == "Sort Mode By Title":
        a = 0
        while a < len(song_list):
            if song_list[a][0][0] == "S":
                cursor_position = a
                print cursor_position
                screen_number = cursor_position / 16
                remainder = cursor_position % 16
                if screen_number == 0:
                    modulus = remainder - 1
                else:
                    modulus = remainder
                screen_display()
                return
            a += 1
    else:
        a = 0
        while a < len(song_list):
            if song_list[a][1][0] == "S":
                cursor_position = a
                print cursor_position
                screen_number = cursor_position / 16
                remainder = cursor_position % 16
                if screen_number == 0:
                    modulus = remainder - 1
                else:
                    modulus = remainder
                screen_display()
                return
            a += 1


def alphabet_sort_jump_t(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    d_key_press = 0
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    w_key_press = 0
    t_key_press += 1
    if t_key_press == 4:
        t_key_press = 1
    if t_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "T":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "T":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if t_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "U":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "U":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if t_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "V":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "V":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def alphabet_sort_jump_w(event=None):  # This function defines the first title for each letter.
    global song_list
    global cursor_position  # This routine sets cursor_position as global variable for use outside of function.
    global screen_number
    global modulus
    global a_key_press
    global d_key_press
    global g_key_press
    global j_key_press
    global m_key_press
    global p_key_press
    global t_key_press
    global w_key_press
    a_key_press = 0  # Resets other multikeys to base letter.
    d_key_press = 0
    g_key_press = 0
    j_key_press = 0
    m_key_press = 0
    p_key_press = 0
    t_key_press = 0
    w_key_press += 1
    if w_key_press == 5:
        w_key_press = 1
    if w_key_press == 1:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "W":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "W":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if w_key_press == 2:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "X":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "X":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if w_key_press == 3:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "Y":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "Y":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1

    if w_key_press == 4:
        if sort_mode == "Sort Mode By Title":
            a = 0
            while a < len(song_list):
                if song_list[a][0][0] == "Z":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1
        else:
            a = 0
            while a < len(song_list):
                if song_list[a][1][0] == "Z":
                    cursor_position = a
                    print cursor_position
                    screen_number = cursor_position / 16
                    remainder = cursor_position % 16
                    if screen_number == 0:
                        modulus = remainder - 1
                    else:
                        modulus = remainder
                    screen_display()
                    return
                a += 1


def rss_writer():  # This function writes rss feeds to Dropbox public directory.

    global text_display_1
    display_info_recover = open("output_list.txt", 'r+')
    output_list_read = display_info_recover.read()
    display_info_recover.close()
    display_info = output_list_read.split(",")
    rss_song_name = display_info[0]
    rss_artist_name = display_info[1]
    rss_current_song = " . . . . . " + str(rss_song_name) + " - " + str(rss_artist_name)
    full_path = os.path.realpath('__file__')  # http://bit.ly/1RQBZYF
    if os.path.exists(str(os.path.dirname("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"))):
        time_now = datetime.datetime.now()
        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.convergencejukebox.com",
            description="",
            lastBuildDate=datetime.datetime.now(),
            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_current_song),
                    link="http://www.convergencejukebox.com",
                    description="Currently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_current_song.xml", "w"))

        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.convergencejukebox.com",
            description="",
            lastBuildDate=datetime.datetime.now(),

            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_song_name),
                    link="http://www.convergencejukebox.com",
                    description="Title Currently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_title_current_song.xml", "w"))

        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.convergencejukebox.com",
            description="",
            lastBuildDate=datetime.datetime.now(),

            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_artist_name),
                    link="http://www.convergencejukebox.com",
                    description="ArtistCurrently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_artist_current_song.xml", "w"))


def check_for_file_change():
    global file_time_old
    file_time_check = str(time.ctime(os.path.getmtime("output_list.txt")))  # http://bit.ly/22zKqLS
    if file_time_old != file_time_check:
        screen_display()  # Updates screen based on file change.
        rss_writer()
        file_time_old = file_time_check
    jukebox_display.after(5000, check_for_file_change)


def so_long(event=None):
    set_default_screen_resolution()
    if os.path.exists(str(os.path.dirname(full_path)) + "\convergenceplayer.py"):
        os.system("player_quit_py.exe")  # Launches Convergence Jukebox Player
        jukebox_display.destroy()
    else:
        os.system("taskkill /im convergenceplayer.exe")
        jukebox_display.destroy()


def set_default_screen_resolution():

    class ScreenRes(object):  # http://bit.ly/1R6CXjF
        @classmethod
        def set(cls, width=None, height=None, depth=32):
            '''
            Set the primary display to the specified mode
            '''
            if width and height:
                print('Setting resolution to {}x{}'.format(width, height, depth))
            else:
                print('Setting resolution to defaults')

            if sys.platform == 'win32':
                cls._win32_set(width, height, depth)
            elif sys.platform.startswith('linux'):
                cls._linux_set(width, height, depth)
            elif sys.platform.startswith('darwin'):
                cls._osx_set(width, height, depth)

        @classmethod
        def get(cls):
            if sys.platform == 'win32':
                return cls._win32_get()
            elif sys.platform.startswith('linux'):
                return cls._linux_get()
            elif sys.platform.startswith('darwin'):
                return cls._osx_get()

        @classmethod
        def get_modes(cls):
            if sys.platform == 'win32':
                return cls._win32_get_modes()
            elif sys.platform.startswith('linux'):
                return cls._linux_get_modes()
            elif sys.platform.startswith('darwin'):
                return cls._osx_get_modes()

        @staticmethod
        def _win32_get_modes():
            '''
            Get the primary windows display width and height
            '''
            import win32api
            from pywintypes import DEVMODEType, error
            modes = []
            i = 0
            try:
                while True:
                    mode = win32api.EnumDisplaySettings(None, i)
                    modes.append((
                        int(mode.PelsWidth),
                        int(mode.PelsHeight),
                        int(mode.BitsPerPel),
                        ))
                    i += 1
            except error:
                pass

            return modes

        @staticmethod
        def _win32_get():
            '''
            Get the primary windows display width and height
            '''
            import ctypes
            user32 = ctypes.windll.user32
            screensize = (
                user32.GetSystemMetrics(0),
                user32.GetSystemMetrics(1),
                )
            return screensize

        @staticmethod
        def _win32_set(width=None, height=None, depth=32):
            '''
            Set the primary windows display to the specified mode
            '''
            # Gave up on ctypes, the struct is really complicated
            #user32.ChangeDisplaySettingsW(None, 0)
            import win32api
            from pywintypes import DEVMODEType
            if width and height:

                if not depth:
                    depth = 32

                mode = win32api.EnumDisplaySettings()
                mode.PelsWidth = width
                mode.PelsHeight = height
                mode.BitsPerPel = depth

                win32api.ChangeDisplaySettings(mode, 0)
            else:
                win32api.ChangeDisplaySettings(None, 0)


        @staticmethod
        def _win32_set_default():
            '''
            Reset the primary windows display to the default mode
            '''
            # Interesting since it doesn't depend on pywin32
            import ctypes
            user32 = ctypes.windll.user32
            # set screen size
            user32.ChangeDisplaySettingsW(None, 0)

        @staticmethod
        def _linux_set(width=None, height=None, depth=32):
            raise NotImplementedError()

        @staticmethod
        def _linux_get():
            raise NotImplementedError()

        @staticmethod
        def _linux_get_modes():
            raise NotImplementedError()

        @staticmethod
        def _osx_set(width=None, height=None, depth=32):
            raise NotImplementedError()

        @staticmethod
        def _osx_get():
            raise NotImplementedError()

        @staticmethod
        def _osx_get_modes():
            raise NotImplementedError()


    if __name__ == '__main__':
        print('Primary screen resolution: {}x{}'.format(
            *ScreenRes.get()
            ))
        print(ScreenRes.get_modes())
        # ScreenRes.set(1280, 720)
        # ScreenRes.set(1920, 1080)
        ScreenRes.set() # Set defaults


file_time_old = "Wed Dec 30 22:56:15 2015"
cursor_position = 0  # Between 0 and end of mp3 library. Used to define what song button is selected
# and the song added to playList from library
screen_number = 0  # Used to determine what screen is displayed.
# Based on cursor_position / 16. 16 is the number of song buttons displayed.
modulus = 0  # Used to determine which of the 16 songs on a screen is active. Based on cursor_position % 16.
credit_amount = 0  # Used to calculate remaining Credits
sort_mode = "Sort Mode By Title"
which_song_number = 0
first_pass = 1  # Used in garbage collection screen_display()
a_key_press = 0
d_key_press = 0
g_key_press = 0
j_key_press = 0
m_key_press = 0
p_key_press = 0
t_key_press = 0
w_key_press = 0
# Following code clears playList and upcoming_list on boot.
play_list = []
upcoming_list = []
# play_list_save = open('c:/media/data/play_list.pkl', 'wb')
play_list_save = open('play_list.pkl', 'wb')
pickle.dump(play_list, play_list_save)
play_list_save.close()
# upcoming_listSave = open('c:/media/data/upcoming_list.pkl', 'wb')
upcoming_listSave = open('upcoming_list.pkl', 'wb')
pickle.dump(upcoming_list, upcoming_listSave)
upcoming_listSave.close()
jukebox_display = tk.Tk()  # Creates a frame whose parent is tk.Tk (that is, root), gives it the name "jukebox_display".
jukebox_display.overrideredirect(1)  # Makes application borderless.
# http://stackoverflow.com/questions/9371663/how-can-i-create-a-borderless-application-in-python-windows
image_file = "jukebox.png"  # this code picks an image file. It can be .bmp, .jpg, .gif. or .png.
image1 = ImageTk.PhotoImage(Image.open(image_file))  # Loads the file and covert it to a Tkinter image object (image1).
# Next two lines get image1 object size.
w = image1.width()  # Assigns the image1 object width to w (variable).
h = image1.height()  # Assigns the image1 object height to h (variable).
# Next two lines are used to create the variables to position coordinates of jukebox_display in the upper left corner.
x = 0
y = 0
jukebox_display.geometry("%dx%d+%d+%d" % (w, h, x, y))  # Code makes the jukebox_display window the size of the image
# by using the variables generated
jukebox_display.state('zoomed')  # Code maximizes the window.
# Next two lines are required because jukebox_display has no image argument. So a label is used as a panel.
panel1 = tk.Label(jukebox_display, image=image1)
panel1.pack(side='top', fill='both', expand='no')
# song_list_recover = open('c:/media/data/song_list.pkl', 'rb')  # Loads song_list.
song_list_recover = open('song_list.pkl', 'rb')  # Loads song_list.
song_list = pickle.load(song_list_recover)
song_list_recover.close()
del song_list_recover
artist_sort()  # Invokes a artist_sort for Jukebox startup. Sort code adapted from
# http://stackoverflow.com/questions/6666748/python-sort-list-of-lists-ascending-and-then-decending
song_list_correction = len(song_list) - 10
last_screen = song_list_correction / 16
if cursor_position == 0:  # this is the startup Jukebox display
    screen_display()
jukebox_display.bind("A", artist_sort)  # Binds artist_sort to A key
jukebox_display.bind("T", title_sort)  # Binds title_sort to T key
jukebox_display.bind("Y", year_sort)  # Binds year_sort to Y key
jukebox_display.bind("x", credit_calculator)  # Binds x to adding credits
jukebox_display.bind("<Down>", down)  # "<Down>" is keyname.
# Info on keynames at http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
jukebox_display.bind("<Up>", up)  # "<Up>" is keyname.
jukebox_display.bind("<Left>", left)  # "<Left>" is keyname.
jukebox_display.bind("<Right>", right)  # "<Right>" is keyname.
jukebox_display.bind("<Escape>", so_long)  # Binds esc key to kill function
jukebox_display.bind("a", alphabet_sort_jump_a)  # Binds a key to a sort function
jukebox_display.bind("d", alphabet_sort_jump_d)  # Binds d key to d sort function
jukebox_display.bind("g", alphabet_sort_jump_g)  # Binds g key to g sort function
jukebox_display.bind("j", alphabet_sort_jump_j)  # Binds j key to j sort function
jukebox_display.bind("m", alphabet_sort_jump_m)  # Binds m key to m sort function
jukebox_display.bind("p", alphabet_sort_jump_p)  # Binds p key to p sort function
jukebox_display.bind("s", alphabet_sort_jump_s)  # Binds s key to s sort function
jukebox_display.bind("t", alphabet_sort_jump_t)  # Binds t key to t sort function
jukebox_display.bind("w", alphabet_sort_jump_w)  # Binds w key to w sort function
check_for_file_change()
jukebox_display.mainloop()  # starts the event (infinite) loop
