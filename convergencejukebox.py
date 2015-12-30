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

import os
from Tkinter import *
import glob
import sys
import time

print "Welcome To Convergence Jukebox"
print "Your Jukebox Is Being Congigured"
print "This Could Take A Few Minutes"
print
print "Convergence Jukebox is Python based codes that emulates a Jukebox and plays mp3 media."
print "Copyright (C) 2012 by Brad Fortner"
print "This program is free software you can redistribute it and/or modify it under the terms"
print "of the GNU General Public License as published by the Free Software Foundation;"
print "either version 3 of the License, or (at your option) any later version."
print "This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied"
print "warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details."
print "You should have received a copy of the GNU General Public License along with this program."
print "If not, see http://www.gnu.org/licenses."
print "The authour, information on, executable downloads and source code can be obtained via www.convergencejukebox.com"

print "Convergence Jukebox employs the PyRSS2Gen Python Library."
print "PyRSS2Gen is copyright (c) by Andrew Dalke Scientific, AB (previously"
print "Dalke Scientific Software, LLC) and is released under the BSD license."
print "Info on PyRSS2Gen at http://www.dalkescientific.com/Python/PyRSS2Gen.html"

time.sleep(10)

full_path = os.path.realpath(
    '__file__')  # http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
artist_list = []

if os.path.exists(str(os.path.dirname(full_path)) + "\music"):
    print "music directory exists at " + str(os.path.dirname(full_path)) + "\music. Nothing to do here."
else:
    print "music directory does not exist."
    os.makedirs(str(os.path.dirname(full_path)) + "\music")
    master = Tk()
    screen_message = "Program Stopped. Please place fifty mp3's in the Convergence Jukebox music directory at " \
                     + str(os.path.dirname(full_path)) + "\music and then re-run the Convergence Jukebox software"
    msg = Message(master, text=screen_message)
    msg.config(bg='white', font=('times', 24, 'italic'), justify='center')
    msg.pack()
    mainloop()
    sys.exit()

mp3_counter = len(glob.glob1(str(os.path.dirname(full_path)) + "\music", "*.mp3"))  # Counts number of MP3 files
current_file_count = int(mp3_counter)  # provides int output for later comparison

if int(mp3_counter) < 50:
    master = Tk()
    screen_message = "Program Stopped. Please place fifty mp3's in the Convergence Jukebox music directory at " \
                     + str(os.path.dirname(full_path)) + "\music and then re-run the Convergence Jukebox software"
    msg = Message(master, text=screen_message)
    msg.config(bg='white', font=('times', 24, 'italic'), justify='center')
    msg.pack()
    mainloop()
    sys.exit()
else:
    print str(os.path.dirname(full_path)) + "\convergenceplayer.py"
    # sys.exit()
    if os.path.exists(str(os.path.dirname(full_path)) + "\convergenceplayer.py"):
        print ".py directory exists at " + str(os.path.dirname(full_path)) + "\convergenceplayer.py"
        os.system("player_launch_py.exe")  # Launches Convergence Jukebox Player
        sys.exit()
    else:
        os.system("player_launch.exe")  # Launches Convergence Jukebox Player
        sys.exit()
