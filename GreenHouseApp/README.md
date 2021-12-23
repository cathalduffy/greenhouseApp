url: https://greenhouse-app.surge.sh/

The Greenhouse App is a simple app that pulls in a number of different functionalities relating to my Raspberry Pi. The idea of the app is to give the user access to their Greenhouse data, to assist in the maintenance of their plants, vegetables, flora, etc.

The app has been deployed using surge.sh, so that it can be accessed from any network.

To begin with, I structured the app using basic HTML and CSS. This provides the basis for the UI to the user. A backend is then provided by using the jQuery library. Upon adding the jQuery library to my project, this has allowed me, through the use of functions, the ability to generate http requests.

Thie app contains four different requests. The first request from my app, is a http GET request that calls the API endpoint that is being transmitted from the IoT application Thingspeak. In turn, Thingspeak is calling data that is being trasmitted from my Raspberry Pi Sensehat. This data contains readings such as the current Temperature, Pressure and Humidity. The script on my Raspberry Pi, to transmit this data, is using the MQTT protocol. This data will also automatically update in my frontend roughly every 5-7 seconds, as I have used the jQuery Ajax function, that allows the data to be received asynchronously, allowing the data to be refreshed in the table, but the user does not have to refresh the page. This is displayed on the 'Home' view in the 'Live Data' table.

The second request from my app, is also another http GET request. This request is targeted again toward data being transmitted by my Raspberry Pi. On my Rapsberry Pi I have a camera streaming script that allows me to transmit a camera stream from my Raspberry Pi. However, due to the fact that this stream was only transmitted on my local environment, I then had to expose this local endpoint through the user of ngrok. Ngrok has allowed me to expose this endpoint and display this camera stream on my app, even when deployed on the world wide web. This is displayed on the 'Camera' view.

The third http request is a http POST request. This POST request targets a script on my Raspberry Pi that allows the user to be able to turn the light on the Sensehat on and off. When the user clicks the 'Light On' button in the app, this triggers the http POST request for the light to turn on and the light will then switch on on my Raspberry Pi Sensehat. The same applies for the 'Turn Off' button, however this will of course trigger a http request to instead turn the light off. This is displayed on the 'Camera' view.

The fourth and final request is a http GET request, once again, to the Thingspeak IoT that display the average readings from the data. Thingspeak offers the user the ability to somewhat build their own request in way, which I have set to the last 120 readings over the past 60 minutes. The data from which can be seen under the 'Average Readings' data table in the frontend.

The app also contains a number of widgets from the Thingspeak IoT such as graphs and gauges displaying the current readings that add a pleasant visual experiensce to the user. 


-------
To start, I need to run both of the following on my Raspberry Pi

jQuery
- Added the jQuery library to the app folder. This library assists in allowing my app to be able to make http requests to both Thingspeak IoT and also to my Raspberry Pi that gives app it's functionality.
From inside the project folder: $ npm install jquery

Send camera data
- from the 'project' folder on my rpi run: $ python3 rpi_camera_surveillance_system.py

Send senseHat data
- from 'project' folder on pi run: $ python3 thingspeak-pub.py mqtt://mqtt3.thingspeak.com:8883
this runs on port 8883

ActivateSenseLight API
- from project folder on pi run: $ python3 sense_api.py
this runs on port 5000

Needed to install jQuery packages to my project folder to use jQuery. I did this through the use of npm.
- $ npm install jQuery

Ngrok
- Install ngrok on raspberry pi to be able to tunnel in to local ports from the internet

- Add port numbers to ngrok authentication script

- Start ngrok on pi, by running: $ ./ngrok start --all

Surge
- Set up the app with Surge to to be able to run on the internet. 
From the inside the project folder, run: $ surge


