__author__ = "Süleyman Bozkurt"
__version__ = "v1.0"
__maintainer__ = "Süleyman Bozkurt"
__email__ = "sbozkurt.mbg@gmail.com"
__date__ = '28.01.2023'
__update__ = '28.01.2023'

import glob
import PyPDF2
import os
import shutil

def main():
    forbidden_chars = '<,>,:,",\,?,/,*,|'
    pdfFiles = glob.glob('*.pdf')

    for pdf in pdfFiles:
        print(pdf)
        file = open(pdf, 'rb')

        # creating a pdf reader object
        reader = PyPDF2.PdfReader(file)

        info = reader.metadata
        title = info.title

        creationdate = str(info['/CreationDate']).split(':')[1][:4]

        author = info.author
        if author == '':
            author = info.creator
            if author == '':
                author = 'None'

        for fb in forbidden_chars:
            title = title.replace(fb, "_")
            author = author.replace(fb, "_")

        file.close()

        # reformated in to new folder
        path = './reformated/'
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
        newPDF_name = f'{author}_{creationdate}_{title}.pdf'
        shutil.copy(pdf, f'{path}{newPDF_name}')


if __name__ == '__main__':
    main()
