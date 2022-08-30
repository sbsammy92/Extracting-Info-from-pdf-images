from pdf2image import convert_from_path
import pytesseract
import util

POPPLER_PATH = r'C:\poppler-21.11.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image

def extract(file_path, file_format):
    # extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path= POPPLER_PATH)
    document_text = ''

    for page in pages:
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text ='\n' + text


    return document_text

    # if file_format== 'prescription':
    #     pass
    # elif file_format=='patient_details'
    #     pass





if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_2.pdf','prescription')
    print(data)