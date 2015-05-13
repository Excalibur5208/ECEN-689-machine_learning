import cv2
from os import listdir
from win32com.client import Dispatch

def resizeFig(pathIn, pathOut):
	# Load an color image in grayscale
	img = cv2.imread(pathIn,0)
	res = cv2.resize(img,(64, 64), interpolation = cv2.INTER_LINEAR)
	cv2.imwrite(pathOut,res)

def method1():
	dir_pre = 'D:/mysite_2/media/'
	dir_1 = 'repository/'
	dir_2 = 'resize_fig/'
	testFileList = listdir(dir_pre + dir_1)
	for name in testFileList:
		pathIn = dir_pre + dir_1 + name
		pathOut = dir_pre + dir_2 + name
		resizeFig(pathIn, pathOut)
	
	h = Dispatch("Matlab.application")
	h.execute("cd 'D:\\mysite_2\\uploads';")
	h.execute("python_matlab('D:\\mysite_2\\media\\resize_fig\\', 'D:\\mysite_2\\media\\result.txt');")

	result_file = open(dir_pre + 'result.txt')
	result = result_file.readlines()
	result_file.close()
	return result
	
def method2():
	dir_pre = 'D:/mysite_2/media/'
	dir_1 = 'repository/'
	
	result_file = open(dir_pre + 'result.txt')
	result = result_file.readlines()
	result_file.close()
	return result


