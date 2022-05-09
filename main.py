from pdfminer.high_level import extract_text
import pyttsx3

text = extract_text("twopage.pdf")

print(text)

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
