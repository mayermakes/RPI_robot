from __future__ import division
import time
from flask import Flask
from flask import render_template
app = Flask(__name__)

import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_stop = 340
#new vars
global lastUD 
lastUD =  340 
global maxUD
maxUD = 600 
global minUD
minUD = 150 
global lastBX
lastBX = 340 
global maxBX
maxBX = 600 

global minBX
minBX = 150 
global lastGO
lastGO = 340
global maxGO
maxGO = 600 
global minGO
minGO = 150
 






def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/command/f")
def commandf():
	#move wheels accordingly to command
	pwm.set_pwm(0, 0, servo_stop + 100)
	pwm.set_pwm(1, 0, servo_stop + 100)
	pwm.set_pwm(2, 0, servo_stop - 100)
	pwm.set_pwm(3, 0, servo_stop - 100)
	time.sleep(1)
	pwm.set_pwm(0, 0, servo_stop)
	pwm.set_pwm(1, 0, servo_stop)
	pwm.set_pwm(2, 0, servo_stop)
	pwm.set_pwm(3, 0, servo_stop)
	time.sleep(1)
	return render_template('index.html')	
	
@app.route("/command/b")
def commandb():
	#move wheels accordingly to command
	pwm.set_pwm(0, 0, servo_stop - 100)
	pwm.set_pwm(1, 0, servo_stop - 100)
	pwm.set_pwm(2, 0, servo_stop + 100)
	pwm.set_pwm(3, 0, servo_stop + 100)
	time.sleep(1)
	pwm.set_pwm(0, 0, servo_stop)
	pwm.set_pwm(1, 0, servo_stop)
	pwm.set_pwm(2, 0, servo_stop)
	pwm.set_pwm(3, 0, servo_stop)
	time.sleep(1)
	return render_template('index.html')	

@app.route("/command/l")
def commandl():
	#move wheels accordingly to command
	pwm.set_pwm(0, 0, servo_stop - 100)
	pwm.set_pwm(1, 0, servo_stop - 100)
	pwm.set_pwm(2, 0, servo_stop - 100)
	pwm.set_pwm(3, 0, servo_stop - 100)
	time.sleep(1)
	pwm.set_pwm(0, 0, servo_stop)
	pwm.set_pwm(1, 0, servo_stop)
	pwm.set_pwm(2, 0, servo_stop)
	pwm.set_pwm(3, 0, servo_stop)
	time.sleep(1)
	return render_template('index.html')	

@app.route("/command/r")
def commandr():
	#move wheels accordingly to command
	pwm.set_pwm(0, 0, servo_stop + 100)
	pwm.set_pwm(1, 0, servo_stop + 100)
	pwm.set_pwm(2, 0, servo_stop + 100)
	pwm.set_pwm(3, 0, servo_stop + 100)
	time.sleep(1)
	pwm.set_pwm(0, 0, servo_stop)
	pwm.set_pwm(1, 0, servo_stop)
	pwm.set_pwm(2, 0, servo_stop)
	pwm.set_pwm(3, 0, servo_stop)
	time.sleep(1)
	return render_template('index.html')	
#new commands

@app.route("/command/u")
def commandu():
	global lastUD
	global maxUD
	global minUD
	#move arm accordingly to command
	lastUD = lastUD + 20
	pwm.set_pwm(4, 0, lastUD )
	
	if lastUD >= maxUD:
		lastUD = (maxUD-20)
	time.sleep(0.5)
	return render_template('index.html')

@app.route("/command/d")
def commandd():
	global lastUD
        global maxUD
        global minUD
	#move arm accordingly to command
	lastUD = lastUD - 20
	pwm.set_pwm(4, 0, lastUD)
	if lastUD >= minUD:
		lastUD = (minUD+20)
	time.sleep(0.5)
	return render_template('index.html')	

@app.route("/command/bo")
def commandbo():
	global lastBX
        global maxBX
        global minBX
	#move arm accordingly to command
	lastBX = lastBX + 20
	pwm.set_pwm(5, 0, lastBX)
	if lastBX >= maxBX:
		lastBX = (maxBX-20)
	time.sleep(0.5)
	return render_template('index.html')

@app.route("/command/ex")
def commandex():
	global lastBX
        global maxBX
        global minBX
	#move arm accordingly to command
	lastBX = lastBX - 20
	pwm.set_pwm(5, 0, lastBX)
	if lastBX >= minBX:
		lastBX = (minBX+20)
	time.sleep(0.5)
	return render_template('index.html')

@app.route("/command/g")
def commandg():
	global lastGO
        global maxGO
        global minGO
	#move arm accordingly to command
	lastGO = lastGO + 10
	pwm.set_pwm(6, 0, lastGO)
	if lastGO >= maxGO:
		lastGO = (maxGO-10)
	time.sleep(0.5)
	return render_template('index.html')

@app.route("/command/o")
def commando():
	global lastGO
        global maxGo
        global minGO
	#move arm accordingly to command
	lastGo = lastGO - 10
	pwm.set_pwm(6, 0, lastGO)
	if lastGO >= minGO:
		lastGO = (minGO+10)
	time.sleep(0.5)
	return render_template('index.html')
	
	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
