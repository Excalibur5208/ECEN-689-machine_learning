import cv2
from os import listdir
from win32com.client import Dispatch

# process the image
img = cv2.imread("img_0.jpg",0)
res = cv2.resize(img,(64, 64), interpolation = cv2.INTER_LINEAR)
cv2.imwrite("img_1.jpg",res)

h = Dispatch("Matlab.application")
h.execute("cd 'D:/2014-2016 TAMU/Course/My course/ECEN689 SPECIAL TOPICS IN MACH LEARNING/8. project/1.task';")
h.execute("python_matlab('img_1.jpg');")

result = open('result.txt')
if int(result.readlines()[0]) == 0:
	print 'cat'
else:
	print 'dog'
result.close()
