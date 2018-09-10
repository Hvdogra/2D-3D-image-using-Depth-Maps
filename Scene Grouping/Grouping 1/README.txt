Dependencies:

1. System wide dependencies
	1. Python 
	2. opencv (along with python bindings, comes together by default)
2. Project dependencies
	(Recommends using python virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs )
	1. All dependencies are enlisted in requirements.txt
		Install them using : pip install -r requirements.txt


Executing the code:

1. Run the main file using python: python main.py -i <input-image>
	* Use 'python main.py -h' for help
	Sample run
		python main.py -i oxford.jpg
			oxford.jpg is there in the same folder.
2. The result will be stored in out.jpg in tbe same folder.
	The ouput image will be as shown in the presentation.


