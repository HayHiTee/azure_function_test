from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def is_this_pdf(passed_file):
    if passed_file.endswith('.pdf'):
        return True


def check_page_number(pdf_file):
    ''' check and return number of pages in pdf file'''
    pdf = PdfFileReader(pdf_file)
    number_of_pages = pdf.getNumPages()
    return number_of_pages


def split_file(pdf_file):
    ''' check if the file has multiple pages and split it if necessary '''

    # fname = os.path.splitext(os.path.basename(path))[0]
    file_name = pdf_file.split('.')[0]
    pdf = PdfFileReader(pdf_file)
    
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(
            file_name, page+1)
            
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

