from PIL import Image
import numpy as np
from numpy import asarray
from imageIdentifier import detection
import os
import fitz
from fitz import Pixmap
def parse_math(pdffile, start, end):
	questionNumOfSection = 0
	def scanPoint(data, startY, startX, identifier):	#compares current alignment of pixels with sought values
		for subY in range(startY, len(identifier)+startY):
			for subX in range(startX, len(identifier[0])+startX):
				if (data[subY][subX] != identifier[subY-startY][subX-startX]):
					return False
		return True


	def scanVertically(data, origData, yl, xl, identifier): #divides images vertically by

		subImgList = []
		tempImgStore = []

		for subScanYLevel in range(yl+1, len(data)-len(identifier)+1-280):
			tempImgStore.append(origData[subScanYLevel][xl:xl+1000])
			if (scanPoint(data, subScanYLevel, xl, identifier) == True):

				for f in range(0, len(tempImgStore)):	#needed incase pixel values are true/false
					for l in range(0, len(tempImgStore[0])):
						if (tempImgStore[f][l] == True):
							tempImgStore[f][l] = [255,255,255]
						elif (tempImgStore[f][l] == False):
							tempImgStore[f][l] = [0,0,0]

				subImgList.append(tempImgStore)
				tempImgStore = []	
			
		for f in range(0, len(tempImgStore)):		#needed for last image, incase values are true/false
			for l in range(0, len(tempImgStore[0])):
				if (tempImgStore[f][l] == True):
					tempImgStore[f][l] = [255,255,255]
				elif (tempImgStore[f][l] == False):
					tempImgStore[f][l] = [0,0,0]

		subImgList.append(tempImgStore) #adds last image becaues the cycle breaks when it hits the bottom
		return subImgList

	def scanImg(filename,questionNumOfSection): 
		imageIdentifier = detection

		col = Image.open(filename) # convert greyscale png to black and white
		gray = col.convert('L')
		bw = gray.point(lambda x: 0 if x<128 else 255, '1')
		bw.save("processed.png")
		
		load = Image.open('processed.png') # convert processed image to list and remove file
		data = asarray(load).tolist()
		os.remove('processed.png')

		load = Image.open(filename) # convert original image to list
		origData = asarray(load).tolist()

		final = []

		for y in range(461,len(data)-len(imageIdentifier)+1-280):	#find starting point
			for x in range(147,len(data[y])-len(imageIdentifier[0])+1-147):
				if (scanPoint(data, y, x, imageIdentifier) == True):
					final.append(scanVertically(data, origData, y,x,imageIdentifier))
					x = x + 1160
					final.append(scanVertically(data, origData, y,x,imageIdentifier))
					break
			break

		for v in range(0, len(final)):
			for x in range(0,len(final[v])):

				questionNumOfSection = 	questionNumOfSection + 1
				array = np.array(final[v][x], dtype=np.uint8)
				new_image = Image.fromarray(array)
				new_image.save(str(questionNumOfSection) + '.png')


	doc = fitz.open(pdffile)
	zoom_x = 4.1666666666  # horizontal zoom
	zomm_y = 4.1666666666  # vertical zoom
	mat = fitz.Matrix(zoom_x, zomm_y)  # zoom factor 2 in each dimension
	
	for z in range(start, end+1):
		page = doc.loadPage(z)
		pix = page.getPixmap(matrix = mat)  # use 'mat' instead of the identity matrix
		output = "page"+str(z)+".png"
		pix.writePNG(output)
		scanImg("page"+str(z)+".png",questionNumOfSection)
		os.remove("page"+str(z)+".png")


			


