from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language = 'en'):
    """Accepts the file path of the pdf and returns an MP3 voiced over version of it"""
    print("Your PDF file is getting processed and getting converted to a MP3")
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        # need to remove space between lines as otherwise we will have pauses in MP3
        text = text.replace('\n','')

        my_audio = gTTS(text=text, lang=language)
        file_name=Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 been saved!'

    else:
        return 'File does not exist, check the files path'

def main():
    file_path = input('Enter a path the PDF file: ')
    language = input("Choose the language of PDF file and produced output, for example en or ru: ")
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()