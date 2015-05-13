import cv2
from os import listdir

def resizeFig(pathIn, pathOut):
	# Load an color image in grayscale
	img = cv2.imread(pathIn,0)
	res = cv2.resize(img,(64, 64), interpolation = cv2.INTER_LINEAR)
	cv2.imwrite(pathOut,res)

def resizeFigBatch():
	str = 'train'
	trainingFileList = listdir(str)
	for name in trainingFileList:
		pathIn = '%s/%s' % (str, name)
		pathOut = 'figs/%s' % (name)
		resizeFig(pathIn, pathOut)

resizeFigBatch()