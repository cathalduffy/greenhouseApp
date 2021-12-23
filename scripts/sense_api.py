#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_cors import CORS
from sense_hat import SenseHat

sense = SenseHat()
deviceID="device1"
#clear sensehat and intialise light_state
sense.clear()

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

@app.route('/sensehat/light',methods=['GET'])
def light_get():
    #check top left pixel value(==0 - off, >0 - on)
    print(sense.get_pixel(0, 0))
    if sense.get_pixel(0, 0)[0] == 0:
        return '{"state":"off"}'
    else:
           return '{"state":"on"}'

@app.route('/sensehat/light',methods=['POST'])
def light_post():
    state=request.args.get('state')
    print (state)
    if (state=="on"):
        sense.clear(255,255,255)
        return '{"state":"on"}'
    else:
        sense.clear(0,0,0)
        return '{"state":"off"}'

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)

