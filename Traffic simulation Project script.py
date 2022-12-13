'''
Wesley Aubynn
202042628
Lab mini project
'''

from engi1020.arduino import *
from time import sleep
#RED signal represented by RED LED pin A0
#YELLOW signal  represened by LCD
#GREEN signal represented by BLUE LED pin  A2
#Button to D5
#Touch sensor to D4
#Servo to D7


def preset():
    lcd_rgb(0,0,0)
    analog_write(2,255)
    analog_write(0,0)
    analog_write(1,0)
    lcd_clear()
    servo_move(7,0)


def yellowSignal(X = 0.5):                  #function for yellow flashing LED cos it will be reused
        analog_write(2,0)
        lcd_rgb(255,255,0)
        sleep(X)
        lcd_rgb(0,0,0)
        sleep(X)


def servoBarriermotion():               #servo barrier motion, increasing by 10 degrees every 3 seconds
    n = 0
    while n < 90:
        n += 7
        if n < 60:
            yellowSignal(0.3)
            servo_move(7,n)
            sleep(0.2)

        else:
            lcd_rgb(0,0,0)
            analog_write(0,255)
            analog_write(2,0)
            servo_move(7,n)
            sleep(1)
    touchPressed = digital_read(3)
    while touchPressed == 1:                          #waiting for the train to finish passing over touch sensor before reverting
        sleep(0.1)
        touchPressed = digital_read(3)





#Function for 15 second LCD countdown display
def LCDcountdown():
    lcd_rgb(10,0,0)
    analog_write(2,0)
    for i in range(15,-1,-1):
        countdown = i
        lcd_print(f"Walk:{countdown}")
        sleep(1)
        lcd_clear()



 # checking if there are pedestrians who want to cross
def buttonStatus():
    buttonPressed = digital_read(5)
    if buttonPressed == 1:
        delay1 = 0
        while delay1 < 6:
            yellowSignal()
            delay1 += 1
        analog_write(0,255)                 #turn red lights on after 5 seconds
        LCDcountdown()
        analog_write(2,255)
    else:
        preset()


# checking if the train is approaching
def trainStatus():
    while True:
        touchPressed = digital_read(3)
        if touchPressed == 1:
            lcd_print("Train")
            lcd_clear()
            servoBarriermotion()
            sleep(5)                            #after train has left sensor, wait 5s before preset
            preset()

        elif touchPressed == 0:
            buttonStatus()
            preset()                                        #green light open barrier


#testing the functions
if __name__ == "__main__":
    #servoBarriermotion()
    #yellowSignal()
    #buttonStatus()
    #LCDcountdown()
    trainStatus()


