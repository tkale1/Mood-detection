README.TXT

AIM: TO DEVELOP A MOOD SENSEING APP

Pre-req

	1.	Google cloud api:
	2.	Google Image library
	3.	Google geoPy library for python
		

HOW TO RUN:

1. Create a virtaul env:
	- cd emotion_detection/
	- sudo pip install virtualenv
	- virtualenv venv

2.	Activate virtual environment
	- source venv/bin/activate

3.	Intall above mentioned pre-req
		- pip install google-cloud
		- pip install image
		- pip install geopy	

4. Add any image file in the project folder

5. Activate Google cloud api key:
	-  export GOOGLE_APPLICATION_CREDENTIALS=apikey.json

6. run the backend program:
	- python face_vision.py

ASSUMPTIONS:

1.	Get the current mood of the user my taking a pic
	Explanition: For this I have used Google Vision API which can detect the current mood of a user based on captured picture or by upload a picture.
	It return distrubuted value of a user's mood most likely ( angry, joy, surprise,sad)

2.	The location of the user(lat/lng) and name of the image file is given (hard coded in the given backend program)
	NOTE: it can be changed to new lat/lng or a new image by changing the value in the main program at line 61 and line 76

Application flow:

1.	Please check the program flow diagram in the main folder.

Completed part:

1. 	Backend program to process image and detect emotion
2.	Fetch user's address from a given lat/lng
3.	Front end which implement with button and camera to click picture of a user

Remaining part:

1. 	Make a get request to from the front to store data on the cloud
2. 	Create RESTapi to get image and lat/lng from the cloud and feed it to backend program.
3.	Process and display results to the front end.
4. validate inputs(if non face image is given in the input the program gives and output of faces found = 0. This can be further used to validate image input.)
5.	Create mood frequency pattern for a given user

API used:

1.	Google Vision API
2.	geopy - a geolocation library for python.
