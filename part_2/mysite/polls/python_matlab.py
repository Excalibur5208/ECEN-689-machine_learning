import cv2
from os import listdir
from win32com.client import Dispatch

def method1():
	# process the image
	img = cv2.imread("img_0.jpg",0)
	res = cv2.resize(img,(64, 64), interpolation = cv2.INTER_LINEAR)
	cv2.imwrite("D:/mysite/polls/img_1.jpg",res)
#	return 'ana'

	h = Dispatch("Matlab.application")
	h.execute("cd 'D:\mysite\polls';")
	h.execute("python_matlab('img_1.jpg');")

	result = open('D:/mysite/polls/result.txt')
	if int(result.readlines()[0]) == 0:
		return 'cat'
	else:
		return 'dog'
''''''