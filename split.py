import fitz
import sys
pdffile = "./data/example.pdf"
doc = fitz.open(pdffile)
page = doc.loadPage(15) #number of page

print(page.getText())
#for page in doc:
    #print(page.getText())
    
""" Code for writing images, to be used later
pix = page.getPixmap()
output = "./images/output.png"
pix.writePNG(output)
"""