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

# <div>Icons made by <a href="http://www.freepik.com" title="Freepik">Freepik</a>
# from <a href="http://www.flaticon.com" title="Flaticon">www.flaticon.com</a> is licensed by
# <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0">CC BY 3.0</a></div>

# This Python script has been tested and compiles into a windows.exe using Pyinstaller.

import os
from Tkinter import *
import glob
import sys
import time
import ctypes
import Tkinter as tk
import convergenceplayer


def get_available_resolutions_win():  # Checks to see if device is 720p compatable for default display.

    class ScreenRes(object):  # http://bit.ly/1R6CXjF
        @classmethod
        def set(cls, width=None, height=None, depth=32):#  Set the primary display to the specified mode
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

        if (1280, 720, 32) in (ScreenRes.get_modes()):
            print "I'm 720p compatable continuing Convergence Jukebox"
        else:
            print "I'm not 720p compatable"
            master = Tk()
            screen_message = "Program Stopped. This computer is not 1280 by 720 (720p) compatable." \
                             " 720p is the default resolution for Convergence Jukebox. This means Convergence Jukebox" \
                             " will not run on this computer. Consult www.convergencejukebox.com if you want more" \
                             " details and a potential fix to the problem."
            msg = Message(master, text=screen_message)
            msg.config(bg='white', font=('times', 24, 'italic'), justify='center')
            msg.pack()
            mainloop()
            sys.exit()


def set_720_resolution():

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
        def _win32_get_modes():#  Get the primary windows display width and height
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
        def _win32_get():#  Get the primary windows display width and height
            import ctypes
            user32 = ctypes.windll.user32
            screensize = (
                user32.GetSystemMetrics(0),
                user32.GetSystemMetrics(1),
                )
            return screensize

        @staticmethod
        def _win32_set(width=None, height=None, depth=32):# Set the primary windows display to the specified mode
            # Gave up on ctypes, the struct is really complicated
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
        def _win32_set_default():#  Reset the primary windows display to the default mode
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
        # print(ScreenRes.get_modes())
        ScreenRes.set(1280, 720)
        # ScreenRes.set(1920, 1080)
        # ScreenRes.set() # Set defaults

# Below is the display mandated by the various software licences used in Convergence Jukebox.
if sys.platform.startswith('linux'):
    print "Welcome to the Linux version of Convergence Jukebox"

if sys.platform == 'win32':
    print "Welcome to the Windows version of Convergence Jukebox"

print "Your Jukebox Is Being Configured"
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

time.sleep(15)

full_path = os.path.realpath('__file__')  # http://bit.ly/1RQBZYF
artist_list = []

if sys.platform == 'win32':
    print "Welcome to the Windows version of Convergence Jukebox"
    user32 = ctypes.windll.user32  # Measure screen resolution. http://bit.ly/1JPUtkd
    screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    get_available_resolutions()
    if str(screen_size) != "(1280, 720)":
        set_720_resolution()

if sys.platform.startswith('linux'):
    root = tk.Tk()
    root.geometry("128000000x72000000")
    tk.Label(text="Checking Your Screen Resolution Maimum Size").pack()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    root.mainloop()
    if screen_width >= 1280 and screen_height >= 720:
        print "This Screen Is 720P compatable"
    else:
        print "I'm not 720p compatable"
        master = Tk()
        screen_message = "Program Stopped. This computer is not 1280 by 720 (720p) compatable." \
                         " 720p is the default resolution for Convergence Jukebox. This means Convergence Jukebox" \
                         " will not run on this computer. Consult www.convergencejukebox.com if you want more" \
                         " details and a potential fix to the problem."
        msg = Message(master, text=screen_message)
        msg.config(bg='white', font=('times', 24, 'italic'), justify='center')
        msg.pack()
        mainloop()
        sys.exit()

if sys.platform == 'win32':
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

if sys.platform.startswith('linux'):
    if os.path.exists(str(os.path.dirname(full_path)) + "/music"):
        print "music directory exists at " + str(os.path.dirname(full_path)) + "Adding underscores to MP3 Files."
        current_path = os.getcwd()
        print current_path
        path = str(current_path) + "/music"
        os.chdir(path)  # sets path for mpg321
        [os.rename(f, f.replace(' ', '_')) for f in os.listdir('.') if not f.startswith('.')]
    else:
        print "music directory does not exist."
        os.makedirs(str(os.path.dirname(full_path)) + "/music")
        master = Tk()
        screen_message = "Program Stopped. Please place fifty mp3's in the Convergence Jukebox music directory at " \
                         + str(os.path.dirname(full_path)) + "\music and then re-run the Convergence Jukebox software"
        msg = Message(master, text=screen_message)
        msg.config(bg='white', font=('times', 24, 'italic'), justify='center')
        msg.pack()
        mainloop()
        sys.exit()

mp3_counter = len(glob.glob1(str(os.path.dirname(full_path)) + "/music", "*.mp3"))  # Counts number of MP3 files
current_file_count = int(mp3_counter)  # provides int output for later comparison

if int(mp3_counter) < 50:
    master = Tk()
    screen_message = "Program Stopped. Please place fifty mp3's in the Convergence Jukebox music directory at " \
                     + str(os.path.dirname(full_path)) + "\music and then re-run the Convergence Jukebox software"
    msg = Message(master, text=screen_message)
    msg.config(bg='white', font=('times', 24, 'italic'), justify='center')
    msg.pack()
    mainloop()
print"Leaving Jukebox"
convergenceplayer()
