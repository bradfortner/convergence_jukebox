import os
import pickle
from Tkinter import *
import ttk
import datetime
import getpass  # Used to get user name http://stackoverflow.com/questions/4325416/how-do-i-get-the-username-in-python

computer_account_user_name = getpass.getuser()
timeDateStamp = datetime.datetime.now().strftime("%A %B %d %Y %I:%M:%S %p")
print timeDateStamp
artistListRecover = open('artist_list.pkl', 'rb')
artistList = pickle.load(artistListRecover)
artistListRecover.close()
aStart = ""
aEnd = ""
bStart = ""
bEnd = ""
cStart = ""
cEnd = ""
dStart = ""
dEnd = ""
eStart = ""
eEnd = ""
fStart = ""
fEnd = ""
gStart = ""
gEnd = ""
hStart = ""
hEnd = ""
iStart = ""
iEnd = ""
jStart = ""
jEnd = ""
kStart = ""
kEnd = ""
lStart = ""
lEnd = ""
mStart = ""
mEnd = ""
nStart = ""
nEnd = ""
oStart = ""
oEnd = ""
pStart = ""
pEnd = ""
qStart = ""
qEnd = ""
rStart = ""
rEnd = ""
sStart = ""
sEnd = ""
tStart = ""
tEnd = ""
uStart = ""
uEnd = ""
vStart = ""
vEnd = ""
wStart = ""
wEnd = ""
xStart = ""
xEnd = ""
yStart = ""
yEnd = ""
zStart = ""
zEnd = ""
numberStart = ""
numberEnd = ""
numberArtist = []
aArtist = []
bArtist = []
cArtist = []
dArtist = []
eArtist = []
fArtist = []
gArtist = []
hArtist = []
iArtist = []
jArtist = []
kArtist = []
lArtist = []
mArtist = []
nArtist = []
oArtist = []
pArtist = []
qArtist = []
rArtist = []
sArtist = []
tArtist = []
uArtist = []
vArtist = []
wArtist = []
xArtist = []
yArtist = []
zArtist = []
numericArtist = []
aToCArtistName = []
dToHArtistName = []
iToMArtistName = []
nToRArtistName = []
sToVArtistName = []
wToZArtistName = []


for i in range(0,len(artistList)-1):
   if artistList[i][0] == "A":
      aArtist.append(artistList[i])
      aToCArtistName.append(artistList[i])
      if aStart == "":
         aStart = i
         numberStart = 0
         numberEnd = i - 1
         aArtist = []
         aToCArtistName = []
         for j in range(numberStart,numberEnd):
            numericArtist.append(artistList[j])
            aToCArtistName.append(artistList[j])
         aArtist.append(artistList[i])
         aToCArtistName.append(artistList[i])
   if artistList[i][0] == "B":
      bArtist.append(artistList[i])
      aToCArtistName.append(artistList[i])
      if bStart == "":
         bStart = i
         aEnd = i - 1
   if artistList[i][0] == "C":
      cArtist.append(artistList[i])
      aToCArtistName.append(artistList[i])
      if cStart == "":
         cStart = i
         bEnd = i - 1
   if artistList[i][0] == "D":
      dArtist.append(artistList[i])
      dToHArtistName.append(artistList[i])
      if dStart == "":
         dStart = i
         cEnd = i - 1
   if artistList[i][0] == "E":
      eArtist.append(artistList[i])
      dToHArtistName.append(artistList[i])
      if eStart == "":
         eStart = i
         dEnd = i - 1
   if artistList[i][0] == "F":
      fArtist.append(artistList[i])
      dToHArtistName.append(artistList[i])
      if fStart == "":
         fStart = i
         eEnd = i - 1
   if artistList[i][0] == "G":
      gArtist.append(artistList[i])
      dToHArtistName.append(artistList[i])
      if gStart == "":
         gStart = i
         fEnd = i - 1
   if artistList[i][0] == "H":
      hArtist.append(artistList[i])
      dToHArtistName.append(artistList[i])
      if hStart == "":
         hStart = i
         gEnd = i - 1
   if artistList[i][0] == "I":
      iArtist.append(artistList[i])
      iToMArtistName.append(artistList[i])
      if iStart == "":
         iStart = i
         hEnd = i - 1
   if artistList[i][0] == "J":
      jArtist.append(artistList[i])
      iToMArtistName.append(artistList[i])
      if jStart == "":
         jStart = i
         hEnd = i - 1
   if artistList[i][0] == "K":
      kArtist.append(artistList[i])
      iToMArtistName.append(artistList[i])
      if kStart == "":
         kStart = i
         jEnd = i - 1
   if artistList[i][0] == "L":
      lArtist.append(artistList[i])
      iToMArtistName.append(artistList[i])
      if lStart == "":
         lStart = i
         kEnd = i - 1
   if artistList[i][0] == "M":
      mArtist.append(artistList[i])
      iToMArtistName.append(artistList[i])
      if mStart == "":
         mStart = i
         lEnd = i - 1
   if artistList[i][0] == "N":
      nArtist.append(artistList[i])
      nToRArtistName.append(artistList[i])
      if nStart == "":
         nStart = i
         mEnd = i - 1
   if artistList[i][0] == "O":
      oArtist.append(artistList[i])
      nToRArtistName.append(artistList[i])
      if oStart == "":
         oStart = i
         nEnd = i - 1
   if artistList[i][0] == "P":
      pArtist.append(artistList[i])
      nToRArtistName.append(artistList[i])
      if pStart == "":
         pStart = i
         oEnd = i - 1
   if artistList[i][0] == "Q":
      qArtist.append(artistList[i])
      nToRArtistName.append(artistList[i])
      if qStart == "":
         qStart = i
         pEnd = i - 1
   if artistList[i][0] == "R":
      rArtist.append(artistList[i])
      nToRArtistName.append(artistList[i])
      if rStart == "":
         rStart = i
         qEnd = i - 1
   if artistList[i][0] == "S":
      sArtist.append(artistList[i])
      sToVArtistName.append(artistList[i])
      if sStart == "":
         sStart = i
         rEnd = i - 1
   if artistList[i][0] == "T":
      tArtist.append(artistList[i])
      sToVArtistName.append(artistList[i])
      if tStart == "":
         tStart = i
         sEnd = i - 1
   if artistList[i][0] == "U":
      uArtist.append(artistList[i])
      sToVArtistName.append(artistList[i])
      if uStart == "":
         uStart = i
         tEnd = i - 1
   if artistList[i][0] == "V":
      vArtist.append(artistList[i])
      sToVArtistName.append(artistList[i])
      if vStart == "":
         vStart = i
         uEnd = i - 1
   if artistList[i][0] == "W":
      wArtist.append(artistList[i])
      wToZArtistName.append(artistList[i])
      if wStart == "":
         wStart = i
         vEnd = i - 1
   if artistList[i][0] == "X":
      xArtist.append(artistList[i])
      wToZArtistName.append(artistList[i])
      if xStart == "":
         xStart = i
         wEnd = i - 1
   if artistList[i][0] == "Y":
      yArtist.append(artistList[i])
      wToZArtistName.append(artistList[i])
      if yStart == "":
         yStart = i
         xEnd = i - 1
   if artistList[i][0] == "Z":
      zArtist.append(artistList[i])
      wToZArtistName.append(artistList[i])
      if zStart == "":
         zStart = i
         zEnd = len(artistList)


class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   root.configure(background="black")
   root.wm_title("Convergence Jukebox Random Play Selector")
   gendresAvailable = ['swing', 'jazz300', 'classiccountry','boomcrooners', 'doowop', 'boomgraffiti', 'elvisera', 'boominstrumentals', 'boomr&b', 'boomboygroups', 'boomgirlgroups', 'beatlesera', 'sixtysampop', 'motown', 'folkera', 'blues', 'showtune', 'classicrock', 'seventyampop', 'disco', 'newwave', 'postdisco', 'newcountry', 'modernrock', 'modernpop', 'canadian', 'christmas', 'hween']
   print gendresAvailable
   lng1 = Checkbar(root, ['Jazz and Swing (All Selections Less Jazz Classics)', 'Top 300 Jazz Classics', 'Classic Country'])
   lng2 = Checkbar(root, ['Crooners', 'Doo-Wop', 'Graffiti', 'Elvis Era', 'Instrumentals', 'Rhythm and Blues', 'Teen Idols', 'Girl Groups', 'British Invasion', '1960s AM Pop', 'Motown Sound'])
   lng3 = Checkbar(root, ['Folk', 'Blues', 'Showtunes', 'Classic Rock', '1970s AM Pop', 'Disco' ])
   lng4 = Checkbar(root, ['New Wave', 'Post Disco', 'New Country', 'Modern Rock', 'Modern Pop'])
   lng5 = Checkbar(root, ['Canadian', 'Christmas', 'Halloween'])
   label0Text = Label(text="Restrict Jukebox Random Selections Up To Five Different Music Genres", bg="black", fg="white", activebackground="black", font=("Helvetica", 18))
   label0Text.pack()
   labelText = Label(text="If More Than Five Selected Only First Five Will Work", bg="black", fg="white", activebackground="black", font=("Helvetica", 18))
   labelText.pack()
   labelTextExtra = Label(text="If No Selections All Jukebox Songs Will Be Played Randomly", bg="black", fg="white", activebackground="black", font=("Helvetica", 18))
   labelTextExtra.pack()
   '''labelTextBlank = Label(text="", bg="black", fg="white", activebackground="black", font=("Helvetica", 18))
   labelTextBlank.pack()'''
   label1Text = Label(text="Pre Baby Boom Era", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label1Text.pack(anchor=W)
   lng1.pack(side=TOP,  fill=X)
   label2Text = Label(text="Early Baby Boom Era", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label2Text.pack(anchor=W)
   lng2.pack(side=TOP,  fill=X)
   label3Text = Label(text="Classic Baby Boom Era", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label3Text.pack(anchor=W)
   lng3.pack(side=TOP,  fill=X)
   label4Text = Label(text="Post Baby Boom Era", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label4Text.pack(anchor=W)
   lng4.pack(side=TOP,  fill=X)
   label5Text = Label(text="Cultural and Calendar", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label5Text.pack(anchor=W)
   lng5.pack(side=TOP,  fill=X)
   #Year Selection Buttons Derrived from Lynda.com video Python GUI Development with Tkinter
   startYear = StringVar()
   comboBoxStart = ttk.Combobox(root, textvariable = startYear)
   comboBoxStart.config(values = ('1910','1911','1912','1913','1914','1915','1916','1917','1918','1919','1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939','1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2009','2010','2011','2012','2013','2014','2015'))
   comboBoxStart.set('Starting Year')
   endYear = StringVar()
   comboBoxEnd = ttk.Combobox(root, textvariable = endYear)
   comboBoxEnd.config(values = ('1910','1911','1912','1913','1914','1915','1916','1917','1918','1919','1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939','1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2009','2010','2011','2012','2013','2014','2015'))
   comboBoxEnd.set('Ending Year')
   label6Text = Label(text="Select Year Range (Optional - No Selections Plays All)", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label6Text.pack(anchor=W)
   comboBoxStart.pack()
   comboBoxEnd.pack()
   label7Text = Label(text="Select Artist From Dropdown Menu's", bg="black", fg="white", activebackground="black", font=("Helvetica", 16))
   label7Text.pack(anchor=W)

   # Year Selection Buttons Derrived from Lynda.com video Python GUI Development with Tkinter

   comboBoxAToC = ttk.Combobox(root, textvariable = aToCArtistName)
   aThruCArtistNames = aToCArtistName
   comboBoxAToC.config(values = (aThruCArtistNames))
   comboBoxAToC.set('Select Artists A thru C')

   comboBoxDToH = ttk.Combobox(root, textvariable = dToHArtistName)
   dThruHArtistNames = dToHArtistName
   comboBoxDToH.config(values = (dThruHArtistNames))
   comboBoxDToH.set('Select Artists D thru H')

   comboBoxIToM = ttk.Combobox(root, textvariable = iToMArtistName)
   iThruMArtistNames = iToMArtistName
   comboBoxIToM.config(values = (iThruMArtistNames))
   comboBoxIToM.set('Select Artists I Thru M')
   
   comboBoxNToR = ttk.Combobox(root, textvariable = nToRArtistName)
   nThruRArtistNames = nToRArtistName
   comboBoxNToR.config(values = (nThruRArtistNames))
   comboBoxNToR.set('Select Artists N Thru R')
   
   comboBoxSToV = ttk.Combobox(root, textvariable = sToVArtistName)
   sThruVArtistNames = sToVArtistName
   comboBoxSToV.config(values = (sThruVArtistNames))
   comboBoxSToV.set('Select Artists S Thru V')
   
   comboBoxWToZ = ttk.Combobox(root, textvariable = wToZArtistName)
   wThruZArtistNames = wToZArtistName
   comboBoxWToZ.config(values = (wThruZArtistNames))
   comboBoxWToZ.set('Select Artists W Thru Z')

   comboBoxAToC.pack()
   comboBoxDToH.pack()
   comboBoxIToM.pack()
   comboBoxNToR.pack()
   comboBoxSToV.pack()
   comboBoxWToZ.pack()
 
   lng1.config(relief=GROOVE, bd=2)
   lng2.config(relief=GROOVE, bd=2)
   lng3.config(relief=GROOVE, bd=2)
   lng4.config(relief=GROOVE, bd=2)
   lng5.config(relief=GROOVE, bd=2)

   def allstates():
       flagList=[]
       flagListTemp=[]
       rawList = list(lng1.state()) + list(lng2.state()) + list(lng3.state()) + list(lng4.state()) + list(lng5.state())
       for i in range(len(rawList)):
           if rawList[i] == True:
               print "Got One"
               flagListTemp.append(gendresAvailable[i])
       if len(flagListTemp) > 5:
           for i in range(5):
               flagList.append(flagListTemp[i])
       else:
           for i in range(len(flagListTemp)):
               flagList.append(flagListTemp[i])
           x = len(flagListTemp)
           for i in range(x,5): #Adds null string to list if not five list elements http://stackoverflow.com/questions/12016005/add-null-character-to-string-in-python
               #flagList.append('\0')
               flagList.append('null')
       #for i in range(6,7):   
       yearStart = comboBoxStart.get()
       yearEnd = comboBoxEnd.get()
       # CSV File writing/updating code
       artistLettersAToC = comboBoxAToC.get()
       artistLettersDToH = comboBoxDToH.get()
       artistLettersIToM = comboBoxIToM.get()
       artistLettersNToR = comboBoxNToR.get()
       artistLettersSToV = comboBoxSToV.get()
       artistLettersWToZ = comboBoxWToZ.get()
       print artistLettersAToC
       print artistLettersDToH
       print artistLettersIToM
       print artistLettersNToR
       print artistLettersSToV
       print artistLettersWToZ

       local = open("genre_flags.txt", "w+")
       s = str(flagList[0]) + "," + str(flagList[1]) + "," + str(flagList[2]) + "," + str(flagList[3]) + "," + str(flagList[4]) + "," + str(yearStart) + "," + str(yearEnd) + "," + str(artistLettersAToC) + "," + str(artistLettersDToH) + "," + str(artistLettersIToM) + "," + str(artistLettersNToR) + "," + str(artistLettersSToV) + "," + str(artistLettersWToZ) + "," + str(timeDateStamp)
       local.write(s)
       local.close()

       print str(flagList[0]+'\n')
       print str(flagList[1]+'\n')
       print str(flagList[2]+'\n')
       print str(flagList[3]+'\n')
       print str (flagList[4]+'\n')
       print str(yearStart+'\n')
       print str(yearEnd+'\n')
       print str(artistLettersAToC+'\n')
       print str(artistLettersDToH+'\n')
       print str(artistLettersIToM+'\n')
       print str(artistLettersNToR+'\n')
       print str(artistLettersSToV+'\n')
       print str(artistLettersWToZ+'\n')
       print str(timeDateStamp+'\n')
            
   labelTextBlank = Label(text="", bg="black", fg="white", activebackground="black", font=("Helvetica", 18))
   labelTextBlank.pack()
   Button(root, text='Enter Selections', command=allstates).pack(side = TOP)
   root.mainloop()

        
