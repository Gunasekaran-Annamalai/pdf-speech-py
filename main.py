import PyPDF2
from gtts import gTTS

pdf_file = open("sample.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

to_speech = None
for i in range(pdf_reader.numPages):
    page = pdf_reader.getPage(i)
    to_speech = gTTS(page.extractText())
    to_speech.save(f'sample{i}.mp3')

pdf_file.close()
