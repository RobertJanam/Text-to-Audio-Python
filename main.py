import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# open
book = askopenfilename()

# read
reader = PyPDF2.PdfReader(book)

# get total pages
pages = len(reader.pages)

# loop through pdf
for n in range(0, pages):
    page = reader.pages[n] # get each page
    text = page.extract_text() # extract text
    # change to audio
    audio_player = pyttsx3.init() # initialize
    audio_player.say(text) # speak
    audio_player.runAndWait()
