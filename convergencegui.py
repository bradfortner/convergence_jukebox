# Convergence Jukebox is Python based codes that emulates a Jukebox and plays mp3 media
# Copyright (C) 2012 by Brad Fortner
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses.
# The authour, information on, executable downloads and source code can be obtained via www.convergencejukebox.com
# Convergence Jukebox employs the hsaudiotag Python library which is released under an OSI BSD licence.
# hsaudiotag see: https://pypi.python.org/pypi/hsaudiotag
# Convergence Jukebox employs the playmp3.py Python library for windows Copyright (c) 2011 by James K. Lawless
# playmp3.py has been released under an MIT / X11 licence. See: http://www.mailsend-online.com/license.php.
# Convergence Jukebox employs the PyRSS2Gen Python Library. PyRSS2Gen is copyright (c) by Andrew Dalke Scientific, AB (previously
# Dalke Scientific Software, LLC) and is released under the BSD license. http://www.dalkescientific.com/Python/PyRSS2Gen.html

import pickle  # Used to save and reload python lists.
# from Tkinter import *
# import FixTk
import tkFont
import base64
from StringIO import StringIO
# import Tkinter
import Tkinter as tk
from PIL import Image, ImageTk
from operator import itemgetter
from ctypes import *  # Used by playmp3.py windows based mp3 player.
# http://www.mailsend-online.com/blog/play-mp3-files-with-python-on-windows.html
import datetime  # Used in RSS generation.
import PyRSS2Gen  # Used n RSS generation.
import getpass  # Used to get user name http://stackoverflow.com/questions/4325416/how-do-i-get-the-username-in-python

computer_account_user_name = getpass.getuser()  # Used to write various log and RSS files to local directories.

winmm = windll.winmm  # Variable used in playmp3.py.


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
    # output_list_recover = open('c:\media\data\output_list.pkl', 'rb')
    output_list_recover = open('output_list.pkl', 'rb')
    display_info = pickle.load(output_list_recover)
    output_list_recover.close()
    del output_list_recover

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
    song_play_mode = display_info[0][5]
    side_line01 = tk.Label(panel1, text=song_play_mode, font="Helvetica 12", background="#161e15", foreground="#81ab49",
                           anchor="nw")
    side_line01.pack()
    side_line01.place(x=40, y=111)

    # Song Title 3rd line on screen
    song_play_mode1 = "Title: " + display_info[0][0]
    side_line02 = tk.Label(panel1, text=song_play_mode1, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line02.pack()
    side_line02.place(x=40, y=131)

    # Song Artist 4th line on screen
    song_play_mode2 = "Artist: " + display_info[0][1]
    side_line03 = tk.Label(panel1, text=song_play_mode2, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line03.pack()
    side_line03.place(x=40, y=151)

    # Release Year/Length 5th line on screen
    song_play_mode3 = "Year: " + str(display_info[0][2]) + "   Length: " + display_info[0][3]
    side_line04 = tk.Label(panel1, text=song_play_mode3, font="Helvetica 12", background="#161e15",
                           foreground="#81ab49", anchor="nw")
    side_line04.pack()
    side_line04.place(x=40, y=171)

    # Album Title 6th line on screen
    song_play_mode4 = "Album: " + display_info[0][4]
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

    # output_list_recover = open('c:/media/data/output_list.pkl', 'rb')
    output_list_recover = open('output_list.pkl', 'rb')
    display_info = pickle.load(output_list_recover)
    output_list_recover.close()
    del output_list_recover

    text_display_1 = display_info[0][0]
    text_display_2 = display_info[0][1]

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
        print "You Have No Credits. Please Insert Coins."
        playMP3('buzz.mp3')
        clear_alpha_keys()
        return
    # play_list_recover = open('c:/media/data/play_list.pkl', 'rb')
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
    # play_list_save = open('c:/media/data/play_list.pkl', 'wb')
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


def get_song_name():  # This function uses the tkInter root after method to read if the outputList has changed.

    global text_display_1
    # output_list_recover = open('c:/media/data/output_list.pkl', 'rb')
    output_list_recover = open('output_list.pkl', 'rb')
    display_info = pickle.load(output_list_recover)
    output_list_recover.close()
    test_string = display_info[0][0]
    print str(test_string)
    test_string2 = display_info[0][1]
    print str(test_string2)
    rss_current_song = " . . . . . " + str(test_string) + " - " + str(test_string2)
    print str(rss_current_song)
    if test_string != text_display_1:
        time_now = datetime.datetime.now()
        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.bradfortner.com",
            description="",
            lastBuildDate=datetime.datetime.now(),
            items=[
                PyRSS2Gen.RSSItem(
                    title=str(rss_current_song),
                    link="http://www.bradfortner.com",
                    description="Currently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_current_song.xml", "w"))

        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.bradfortner.com",
            description="",
            lastBuildDate=datetime.datetime.now(),

            items=[
                PyRSS2Gen.RSSItem(
                    title=str(test_string),
                    link="http://www.bradfortner.com",
                    description="Title Currently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_title_current_song.xml", "w"))

        rss = PyRSS2Gen.RSS2(
            title="Convergence Music System RSS Feed Current Song",
            link="http://www.bradfortner.com",
            description="",
            lastBuildDate=datetime.datetime.now(),

            items=[
                PyRSS2Gen.RSSItem(
                    title=str(test_string2),
                    link="http://www.bradfortner.com",
                    description="ArtistCurrently Playing",
                    pubDate=datetime.datetime(int(time_now.year), int(time_now.month), int(time_now.day),
                                              int(time_now.hour), int(time_now.minute))),
            ])

        rss.write_xml(open("c:\\users\\" + computer_account_user_name + "\\Dropbox\\public\\"
                           + computer_account_user_name.lower() + "_artist_current_song.xml", "w"))

        test_string = ""
        text_display_1 = ""
        screen_display()

    jukebox_display.after(5000, get_song_name)  # reschedule event in 2 seconds
    # If it has the routine will update the jukebox screen accordingly.
    # From http://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop.


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
# image_file = "jukebox.png"  # this code picks an image file. It can be .bmp, .jpg, .gif. or .png.
background_base64 = "iVBORw0KGgoAAAANSUhEUgAABQAAAALQCAYAAADPfd1WAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAB8FpJREFUeNrs3QmAXFWZPvzn1q197TWdhKxkBUJCwhIW2UUUEWVcAMVBEBxRR0E//zqj6LiMOoojCjqogBuLio46IqDgqIwgKARZZDNAQvaks/Ve6/3ue26d6tM31UkndNK1PD8sq/rWdutUpeo9733PORaAh91TBkRERERERERERNRwgu7Jdk9z2RRERERERERERESNJ8AmICIiIiIiIiIialxMABIRERERERERETUwJgCJiIiIiIiIiIgaGBOAREREREREREREDYwJQCIiIiIiIiIiogbGBCAREREREREREVEDYwKQiIiIiIiIiIiogTEBSERERERERERE1MCYACQiIiIiIiIiImpgTAASERERERERERE1MCYAiYiIiIiIiIiIGhgTgERERERERERERA2MCUAiIiIiIiIiIqIGxgQgERERERERERFRA2MCkIiIiIiIiIiIqIExAUhERERERERERNTAmAAkIiIiIiIiIiJqYEwAEhERERERERERNTAmAImIiIiIiIiIiBoYE4BEREREREREREQNjAlAIiIiIiIiIiKiBsYEIBERERERERERUQNjApCIiIiIiIiIiKiBMQFIRERERERERETUwJgAJCIiIiIiIiIiamBMABIRERERERERETUwJgCJiIiIiIiIiIgaGBOAREREREREREREDYwJQCIiIiIiIiIiogbGBCAREREREREREVEDYwKQiIiIiIiIiIiogTEBSERERERERERE1MCYACQiIiIiIiIiImpgTAASERERERERERE1sCCbgIiIiMaTZVlwHGcP11vupZK6bNsWisUS9D0CAfcaR24HOKWR9w3YNkrFovFY3m3UuTP83FbA+3v0fdC3Hz4X+j5qH0ojb7u77f7HlpPcLlDeD/N27kuAvAT/ebX9G/Hajeeu9jr09dWea7T7V3ts/Vhjud9obVOtncx2Yfux/dh+bD+2H9tvrO1Xbbv5m20+ZsCSmMIZ/Tl9j+tvL/08ZvuPeB8RcK8vudd752bcM9r7SlQzMbp7etQ9HcGmICIiogPJDJ7lsiQFJYj2tpVG3M4yAnrb7ZU4JTcEV52TIiKRiHueRzgcRi43pG4r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"
image_file = StringIO(base64.decodestring(str(background_base64)))
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
jukebox_display.bind("a", alphabet_sort_jump_a)  # Binds a key to a sort function
jukebox_display.bind("d", alphabet_sort_jump_d)  # Binds d key to d sort function
jukebox_display.bind("g", alphabet_sort_jump_g)  # Binds g key to g sort function
jukebox_display.bind("j", alphabet_sort_jump_j)  # Binds j key to j sort function
jukebox_display.bind("m", alphabet_sort_jump_m)  # Binds m key to m sort function
jukebox_display.bind("p", alphabet_sort_jump_p)  # Binds p key to p sort function
jukebox_display.bind("s", alphabet_sort_jump_s)  # Binds s key to s sort function
jukebox_display.bind("t", alphabet_sort_jump_t)  # Binds t key to t sort function
jukebox_display.bind("w", alphabet_sort_jump_w)  # Binds w key to w sort function
get_song_name()
jukebox_display.mainloop()  # starts the event (infinite) loop