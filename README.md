#Docker_Hub_Project

How to run tests:

- Install Python 3.5.2 (https://www.python.org/downloads/) 
	- Select 'Add Python 3.5 to PATH' option
- Download chrome driver and put it under Python Folder (https://chromedriver.storage.googleapis.com/index.html?path=2.25/)
- Open command line and run the command below:
	- pip install selenium
- To run the test, save the folder on PC. Then from command line, go to the folder and run below command:
	- python Docker_Testcases.py >log.txt
	- Test should run on chrome and print output log.txt file.
	- In command line, if all test passed, it should show: 
		Ran 5 tests in __s
		OK
	- If any test fails, it should show:
		Ran 5 tests in __s
		FAILED (errors='no of tests failed')
