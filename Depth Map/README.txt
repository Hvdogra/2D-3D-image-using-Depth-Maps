Dependencies:

1. System wide dependencies
	1. Python 
	2. opencv (along with python bindings, comes together by default)
2. Project dependencies
	(Recommends using python virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs )
	1. All dependencies are enlisted in requirements.txt
		Install them using : pip install -r requirements.txt


Executing the code:

1. Run the main file using python: python heightDepthCue.py <inputimage1> <inputimage2> <vanishing point coordinates>
	Sample run
		python heightDepthCue.py color_img1.jpg out.jpg 900 -3537
			color_img1.jpg is there in the same folder and represents the Salient Region segmented image.
			out.jpg is the scene grouping image.
			900 is coordinate along width(horizontal direction)
			-3537 is coordinate along height(vertical direction)
2. The result of depth map will be stored in newImg6.jpg in tbe same folder.
	The ouput images will be as shown in the presentation.


