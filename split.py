from pdf2image import convert_from_path #https://stackoverflow.com/questions/46184239/extract-a-page-from-a-pdf-as-a-jpeg
pages = convert_from_path('./data/example.pdf', 500)