from openalpr import Alpr
from picamera import PiCamera
from time import sleep
import subprocess
import requests
import json

# 'us' means we want to recognise USA plates, many others are available
alpr = Alpr("us", "/etc/openalpr/openalpr.conf",
            "/usr/share/openalpr/runtime_data")
camera = PiCamera()

# IP Address will be changed by network change depends on PC's IP
URLSelect = 'http://192.168.0.164:80/select'
URLInsert = 'http://192.168.0.164:80/insert'

try:
    # Let's loop forever:
    while True:

        # Take a photo
        print('Taking a photo')

        camera.capture('/home/pi/latest.jpg')

#	opens a window in order to show photo that is taken
#	image = subprocess.Popen(["feh", "--hide-pointer", "-x", "-q", "-B", "black", "-g", "1280x800", "/home/pi/latest.jpg"])

        # Ask OpenALPR what it thinks
        analysis = alpr.recognize_file("/home/pi/latest.jpg")

        # If no results, no car!
        if len(analysis['results']) == 0:
            print('No number plate detected')

        else:
            number_plate = analysis['results'][0]['plate']
            print('Number plate detected: ' + number_plate)
            licenseplate = number_plate
            PARAMS = {'licenseplate':licenseplate}
	    try:
            	r = requests.get(URLSelect, PARAMS, timeout=2)
		data = json.loads(r.text)
		#print(data)
	    except requests.exceptions.ConnectionError:
	        print(r.status_code)

	    if data['found'] == '0':

		print("License Plate Could not Found!\nAdd it now;")
                name = raw_input("Whose Car is This?: ")
		PARAMS = {'licenseplate':licenseplate, 'name':name}
		r = requests.get(URLInsert, PARAMS, timeout=2)
		print("Welcome on Board " + licenseplate + " , " + name + "!")

            else:
                licenseplate = data['licenseplate']
                name = data['name']
                print("License Plate Found: " + licenseplate)
                print("Registered Name on Plate: " + name)

#	closes the window that shows the photo
#	image.kill()
        # Wait for one seconds
        sleep(1)

except KeyboardInterrupt:
    print('Shutting down')
    alpr.unload()

