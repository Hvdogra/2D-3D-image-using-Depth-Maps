Dependencies:

1. System wide dependencies
	1. Python 3.5+
	2. opencv (along with python bindings, comes together by default)
2. Project dependencies
	(Recommends using python virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs )
	1. All dependencies are enlisted in requirements.txt
		Install them using : pip install -r requirements.txt


Executing the code:

1. Run the main file using python3: python3 main.py -i <input-image>
	* Will provide a minimal GUI to mark the seed pixels. While marking, switching between "background" and "object" pixels are done using keys 'b' and 'o' respectively. By default GUI initializes in object mode. Object is marked with "red" markings and Background with "blue".
	* Use 'python3 main.py -h' for help
	Sample run
		python main.py -i download.jpeg
			download.jpeg is there in the same folder.
2. Press ESC after marking the seeds.
3. Output window will provide the results.
4. Output image will be written in running folder, named "out.png"
5. Now, run the problem.py as
		python problem.py
	make sure that the input to problem.py is same as output of fast_seg.py(already set by default for this case).

	The ouput images will be as shown in the presentation.


