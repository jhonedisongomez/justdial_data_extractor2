# justdial_data_extractor2
STEPS TO CONFIG THE EXTRACTOR DATA JUSDIAL

To run the project we have to do the following steps:

1- install python 2.7 or a version above
2- inside the root folder project we have to run the following comands
	
	a. pip install virtualenv
	b. virtualenv .env
	c. cd .env/Scripts
	a. activate

after execute the comands in the cmd, return to the root folder

3- execute the comand pip install -r requiriments.txt to install all enviroment to the project
4- Download the chrome driver from the following page:
https://chromedriver.storage.googleapis.com/index.html?path=2.33/

after to do it, decompress the chromedriver in this path .env/selenium/webdriver. when the process finish, the folder webdriver must have a file with name chromedriver.exe
5- go to path-project/crawler_manager and open the file views.py, search the variables driver and driver2 and change the path webdriver eg: driver = ("path-project/.env/selenium/webdriver"), these are 4 changes in the file.
6- open the initServer.bat, it is inside the root path project and change the path to the real path project in us local system.