# convergence_jukebox
Convergence Jukebox is a fully functional retro jukebox application. It emulates "physical" jukeboxes and is written in Python. The software has been designed to be fully functional, playing mp3's both randomly and via a credit system. More at www.convergencejukebox.com
If you’re a fan of old Jukeboxes, especially a form of Jukebox know as a wallbox, then Convergence Jukebox is for you. Convergence Jukebox is open source Python software that has been written to emulate those “retro” style wallboxes that were popular in bars, restaurants and recreation areas during the 1950’s and 60’s. 

Written from scratch and field tested over the past three years, Convergence Jukebox plays properly formed ID3 tagged mp3 media. The Jukebox can be controlled for “personal” use by your computer keyboard but is better operated with a USB keypad. Its output resolution is modifiable allowing it to connect to inexpensive computer, laptop or TV displays with its “retro look and feel”. It can even be connected to bill, coin or card acceptors for “pay to play” situations.

Features included in the initial release of Convergence Jukebox are quite extensive and are as follows;

Unlimited mp3 library size: Currently operating a version containing over 8000 mp3 files. This implementation runs on minimum hardware. In this case it’s an Raspberry Pi 1 model B revision 2 with 512 MB ram and a ‎64.0 GB SD card.

Automatic Song Detection: MP3 library database is built automatically when additional properly formed ID3 tagged files are added to the media folder and the program is restarted.

Multiple Display Resolutions: Developers can change display resolution, skins and customize all items on the screen (such as song name positions) using Pythons Tkinter code.

Customizable To Your Location: The Jukebox name or service at top of arch can be customized in the Python Tkinter code.

Background Music System: Convergence Jukebox plays library loaded in Jukebox in a continuous manner randomly. Makes an excellent background music system.

Different Styles Of Music: mp3’s can be tagged with genres in comment area of ID3 tag. Random play can be set to play specific genres by altering a simple text file.

Songs Can Be Skipped: mp3’s can be tagged “norandom” meaning they will never play randomly. This means mp3’s with potentially unsuitable content can only be played if selected.

Avoids Repeating The Same Songs Continuously: mp3’s on the random list are only played once during a random play cycle.

Automatic Resetting Of Random List: Convergence Jukebox resets the random list when the software is rebooted or when all selections in the jukebox have been played once randomly.

Clearly Identified Songs: While song is playing, song title and artist are displayed prominently under the Jukebox arch on the display.

More detailed song information is displayed in the green display (top left) that includes year released, song length and album name pulled from the mp3 id3 tags.

Convergence Jukebox plays user selected songs (paid) as a priority: When selected songs are listed in order of selection under the Upcoming Selections heading in the status area.

Users cannot select the same song if it’s on the Upcoming Selections list. This eliminates the same song from being played repeatedly.

Songs played via selection are removed from the random playlist. This eliminates the same song from being played repeatedly.

Random play resumes once user selected songs have completed playing.

Number of Credits, cost per credit and the number of songs available in the library are clearly displayed (and editable in the Python code) at the bottom left of the green screen.

Users can navigate through available music using up/down/left/right navigation keys.

Users can navigate through music selecting songs by either Title or Artist.

Users can navigate to the alphabetical start of either Artist or Title using specific letter keys that employ multiple keypresses.

A log is kept of each song played randomly, each song paid to play, when the Jukebox is rebooted, when songs are added and when a new random list is generated.

Their is Python code buried in the release that’s not been documented that talks to a Dropbox folder to providing RSS feeds for digital signage systems.

The latest release of Convergence Jukebox is now fully operational on either a Raspberry Pi 1 or 2 running Raspian. The Convergence Jukebox source code is distributed from its GitHub page to encourage others to further modify the software, adapt it to other platforms and to add features.

Convergence Jukebox is licensed with a GNU V3 General Public License that guarantees end users (individuals, organizations, companies) the freedoms to run, study, share (copy), and modify the software. It’s perfectly suited as a Jukebox software base for the Maker community as its Python code can be easily modified and adapted.

More information on Convergence Jukebox can be found at www.convergencejukebox.com including links to its GitHub site and posts on how to use Convergence Jukebox.
