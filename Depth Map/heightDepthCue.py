import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(10000000)#set recursion limit
name1 = sys.argv[1]			#input file 1
name2 = sys.argv[2]			#input file 2
img = cv2.imread(name1)
img1 = cv2.imread(name2)
gray0 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)			# load grayscale images
# gray6 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("old",gray3)
gray4 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray5 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# cv2.imwrite('img.jpg',gray)

height, width = gray.shape
print height, width					#print height and width of image

#For Relative height Depth cue
for i in range(0, height):
	for j in range(0, width):
		gray[height-i-1, j] = 255*(height-i)/height

cv2.imwrite('heightDepthCue.jpg',gray)

#Euclidean depth hypothesis
xi=int(sys.argv[3])		#Vanishing point coordinates
yj=int(sys.argv[4])
max = -1
matrix = [[0 for x in range(width)] for y in range(height)] 
for i in range(0, height):
	for j in range(0, width):
		matrix[i][j] = np.sqrt((i-xi)**2 + (j-yj)**2)
		# print matrix[i][j]
		if(matrix[i][j]>max):
			max = matrix[i][j]
		# gray1[i][j] = (gray1[i][j]*255/max)

for i in range(0, height):
	for j in range(0, width):
		gray1[i][j] = (matrix[i][j]*255)/max
			
cv2.imwrite('euclideanDepth.jpg',gray1)

#combined depth hypothesis
xi = float(xi)
weightR = xi/(2*height)
print weightR
weightH = 1-weightR
for i in range(0, height):
	for j in range(0, width):
		gray2[i][j] = weightR*gray[i][j] + weightH*gray1[i][j]

cv2.imwrite('combinedDepth.jpg',gray2)
# gray2f = gray2.astype('float')
# gray3f = gray3.astype('float')
# additionF = (gray2f+gray3f)/2
# gray4 = additionF.astype('uint8')

#Local depth hypothesis
for i in range(0, height):
	for j in range(0, width):
		grayf = gray[i][j].astype('float')
		gray2f = gray2[i][j].astype('float')
		gray3f = gray3[i][j].astype('float')
		if(gray3f == 0.0):
			additionF = grayf+gray3f
		else:
			additionF = (gray2f+gray3f)/2
		gray4[i][j] = additionF.astype('uint8')

cv2.imwrite('localDepth.jpg',gray4)
gray6 = gray4
# for i in range(0, height):
# 	for j in range(0, width):
# 		gray4[i][j] = gray2[i][j]+gray3[i][j]
# 		# x = np.uint8(gray2[i][j])
# 		# y = np.uint8(gray3[i][j])

# 		print cv2.add(x,y)
# 		# if(gray2[i][j]+gray3[i][j]>uint_8(255)):
# 		# 	print gray2[i][j]+gray3[i][j], gray4[i][j]

 # A function to check if a given cell 
    # (row, col) can be included in DFS
def isSafe(i, j, visited):
# row number is in range, column number
# is in range and value is 1 
# and not yet visited
	return (i >= 0 and i < height and
	j >= 0 and j < width and
	not visited[i][j])
             
#for static variable in python
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

#DFS Recursive algorithm
@static_vars(var=1)
def DFS(i, j, visited, count, list):
 
        # These arrays are used to get row and 
        # column numbers of 8 neighbours 
        # of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]
        # prev = count
        list.append([i,j])
        DFS.var = 1
        count = count+1
        # max = count
        # Mark this cell as visited
        visited[i][j] = True
        # print gray5[i][j]
        # print DFS.var
        # Recur for all connected neighbours
        for k in range(8):
            if isSafe(i + rowNbr[k], j + colNbr[k], visited) and gray5[i][j] == gray5[i + rowNbr[k]][j + colNbr[k]] and gray0[i][j]>0:
                DFS(i + rowNbr[k], j + colNbr[k], visited, count,list)
        if(DFS.var == 1):
        	# print "Count is ",count
        	sum = 0
        	value = 0
        	for pair in list:
        		sum = sum+gray2[pair[0]][pair[1]]
        		value = value + 1
        	sum = sum/(value+0.05)
        	if sum > 255:
        		for pair in list:
        			print (gray5[pair[0]][pair[1]]+gray2[pair[0]][pair[1]])/2
        		sum = 255
        	for pair in list:
        		grayf = gray5[pair[0]][pair[1]].astype('float')
        		gray2f = gray2[pair[0]][pair[1]].astype('float')
        		#additionF = (gray2f+grayf)/2
        		additionF = sum
        		gray6[pair[0]][pair[1]] = additionF.astype('uint8')
        		# gray6[pair[0]][pair[1]] = (gray5[pair[0]][pair[1]]+gray2[pair[0]][pair[1]])/2
        	
        DFS.var = 0 		


# cv2.imwrite('newImg4.jpg',gray4)
# cv2.imwrite('newImg54.jpg',gray5)
visited = [[False for j in range(width)]for i in range(height)]
for i in range(0, height):
	for j in range(0, width):
		if(gray0[i][j]>0):
			if visited[i][j] == False:
				count = 0
				list = []
				DFS(i, j, visited, count, list)

cv2.imwrite('depthMap.jpg',gray6)
cv2.waitKey()
# print count, " ", height*width, " ", count/(height*width)
#you need to set the thresholding parameters 
# ret, thresh = cv2.threshold(gray,50,127,cv2.THRESH_BINARY)
# cv2.imwrite('img1.jpg',thresh)

# #you need to set the size of the kernel for closing
# kernel = np.ones((50,50), np.uint8)
# open1 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# cv2.imwrite('color_img1.jpg', open1)
# cv2.waitKey()(732.0, 924.0)
