import fitz
import sys
import re
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


questions = dict() # Fix this constructor or something

pdffile = "./data/example.pdf"  # Some url to PDF
doc = fitz.open(pdffile)        # This is a generator.
page = doc.loadPage(1)          # Load some page
pages=[]                        # Array of all pages
for page in doc:                # Init pages
    pages.append(page.getText())

# Create a generic question object
class Question:
    num = 0         # Question number
    choices = []    # String[] of possible choices - [] be used as an FRQ for math?
    answer = ""     # String from choices that is the correct answer 

    def __init__(self, num, choices, answer):
        self.num = num
        self.choices = choices
        self.answer = answer

# Reading parser
def parse_reading(start, end):
    keyword = " are based on the following \npassage" 
    
    reading_pages = pages[start:end]
    reading = {}
    # reading.update(section : passage : [ "",{ qnumber : [question,answer]}])
    currentpassage = currentquestion = 0
    searching_question = False
                    
        #So, I *think* questions are going to look like questionNum\n\n\n?

    for page in reading_pages:
        if not searching_question: 
        
            # If this is the start of a passage:
            if keyword in page.lower():         # Start the construction for a passage start
                page = page.split(keyword)[1]   # Remove the bits before the reading passage
                # Increment passage & question
                currentpassage += 1
                currentquestion += 1
                # Add the passage to the array and set it to the current one
                reading.update( {str(currentpassage) : ["", {}]} )
                #passage = reading[currentpassage][0] #I think this is the problem. You can't assign to a mem location like this in python? smh

                formattedquestion = "\n{0}".format(currentquestion)
                if  re.search("A\).*\\nB\).*\\nC\).*\\nD\).*",page) != None:
                    reading[str(currentpassage)][0] += page
                    searching_question = True # Once we hit the end phrase, start scanning the PDF for questions.
                else:
                    reading[str(currentpassage)][0] += page 

            # If this is a page of questions following a passage:
            elif currentpassage > 0:
                
                if "nigeria" in page.lower():
                    x=re.findall("\\nA\).*\\nB\).*\\nC\).*\\nD\).*",page)
                    if x != None:
                        print(x)
                        print("EE")
                    
                # Format question and set current passage
                formattedquestion = "\n{0}".format(currentquestion)
                if re.search("A\).|\\n*B\).|\\n*C\).|\\n*D",page) != None:
                    reading[str(currentpassage)][0] += page[:re.search("A\).|\\n*B\).|\\n*C\).|\\n*D",page).span()[0]]
                    searching_question = True
            

               
 
        while(searching_question and currentpassage>0):
            if "nigeria" in page.lower():
                print(currentquestion)
            try:
                start = page.index("{0}\n\n".format(currentquestion))
            except:
                searching_question=False
            try:
                index = page.index("{0}\n\n".format(currentquestion+1)) # If the next question is on this page, call recursively
                if index != -1: 
                    reading[currentpassage][1].update({str(currentquestion) : page[start:index] })
                    currentquestion+=1
            except:
                reading[str(currentpassage)][1].update({str(currentquestion) : page[start:] })
                currentquestion+=1
                searching_question=False
    return reading
    

    
# I think I know.

#Writing parser

#Math parser

#CalcMath parser

start=end=0
for num,page in enumerate(pages):
    if("reading test" in page.lower()):
        start=num
    if("writing and language test" in page.lower()):
        end=num-1
if (start != 0 and end !=0):
    print(parse_reading(start,end)["1"][0])
    #Qi, you there?  Anything wrong? You okay? I'm going to takea  break for a bit too, message you soon.
    
"""
pix = page.getPixmap()
output = "./images/output.png"
pix.writePNG(output)
""" 