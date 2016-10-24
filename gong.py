#!/usr/bin/python
# 2014 Wells Riley

import pigpio
import time
import thread

PIN = 4
LEFT = 1000
RIGHT = 2000
CENTER = LEFT + ((RIGHT - LEFT)/2)
STEP=100
SLEEP=0.01

pigpio = pigpio.pi()
pigpio

def init_servo():
	pigpio.set_PWM_frequency(PIN, 50) # 50Hz pulses
	pigpio.set_PWM_range(PIN, 20000) # 1,000,000 / 50 = 20,000us for 100% duty cycle
  	print 'Initializing...'
  	move_servo(CENTER)

def move_servo(duty_cycle_us=0):
	pigpio.set_servo_pulsewidth(PIN, duty_cycle_us)
	time.sleep(SLEEP)

def spin_servo_cw_from(start, end):
	for duty_cycle_us in range(start, end+STEP, STEP):
		move_servo(duty_cycle_us)

def spin_servo_ccw_from(start, end):
  for duty_cycle_us in range(start, end-STEP, -STEP):
  	move_servo(duty_cycle_us)

def stop_servo():
  move_servo(CENTER)
  pigpio.set_servo_pulsewidth(PIN, 0)

def gong():
  init_servo()
  print 'Initialized!'
  time.sleep(0.1)

  spin_servo_ccw_from(CENTER,LEFT)
  print 'Spinning to left...'
  spin_servo_cw_from(LEFT,CENTER)
  print 'Spinning to right...'


gong()

stop_servo()
print 'Spinning to center...'

pigpio.stop()
print "Cleaning up..."
print "Done"
