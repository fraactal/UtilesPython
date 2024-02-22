import pyttsx3, PyPDF2
from icecream import ic 

#pdfreader = PyPDF2.PdfFileReader(open('El_Kybalion.pdf', 'rb'))
pdfreader = PyPDF2.PdfReader(open('El_Kybalion.pdf', 'rb'))

ic(pdfreader)

speaker = pyttsx3.init()

for page_num in range (pdfreader.numPages):
#for page_num in range (pdfreader.):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n',' ')
    print(clean_text)


speaker.save_to_file(clean_text,'El_Kybalion.mp3')
speaker.stop()
speaker.runAndWait()

'''
To install espeak on ubuntu or any of the debian based OS, enter the following command on the terminal:

sudo apt install espeak
To use pyttsx3 python library, install the following using terminal:

pip3 install pyttsx3 sudo apt install espeak pip3 install pyaudio or use sudo apt install python3-pyaudio


'''