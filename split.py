import fitz
import sys
"""
https://github.com/pymupdf/PyMuPDF-Utilities/tree/master/examples
Steps:
  Prepass:
    Figure out which pages have tables and set them for later handling; put them through some separate functions to handle that. Certain diagram pages (see 28) are a mix of text and diagrams... we'll need to give parsing these more thought.
    Parse images/map them to pages in the big dict. (b64?)
  Primary pass:
    Dump all of the nondiagram pages to image first, save them to the images dir.
    Dump all of the text and cut out "unauthorized use" etc as well as page number + asterisk divisors + "continue" + "stop" + headers. (which should be used internally to decide when certain segments are over)
    Split it into text portions and questions portions. Put them under test "directories" in a big JSON.
    
    Figure out some way to parse inline numbers. I.e: 12 bird. This was a bird that was... (see page 22 of the PDF)


"""




pdffile = "./data/example.pdf"
doc = fitz.open(pdffile)
page = doc.loadPage(21) #number of page

print(page.getText())
#for page in doc:
    #print(page.getText())

    
""" Code for writing images, to be used later
pix = page.getPixmap()
output = "./images/output.png"
pix.writePNG(output)
"""
