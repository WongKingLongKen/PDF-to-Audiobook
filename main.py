# read English words
import pyttsx3
import PyPDF3
import pdfplumber

file = 'Ch.1.pdf'

book = open(file, 'rb')
pdfreader = PyPDF3.PdfFileReader(book)
pages = pdfreader.numPages
engine = pyttsx3.init()

finalText = ""

with pdfplumber.open(file) as pdf:
    for num in range(0, pages):
        page = pdf.pages[num]
        text = page.extract_text()
        finalText += text

engine.setProperty("rate", 150)
# engine.save_to_file(finalText, 'Ch.1.pdf') for saving the audiobook
# otherwise
engine.say(finalText)
engine.runAndWait()