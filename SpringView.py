import time
import board
import digitalio
import neopixel

# LED setup.
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# BUTTON_A is an reference to the 2 buttons on the Circuit Python Express
switch = digitalio.DigitalInOut(board.BUTTON_A)
switch.direction = digitalio.Direction.INPUT

# pull controls the electrical behavoir of the pin
# The standard Pull.DOWN as electricity flows through the pin, switch.value = False(LOW), When the button is pressed, switch.value = True(HIGH)
switch.pull = digitalio.Pull.DOWN
# Pull.UP inverses the behavior and enables the built in resistor
ispressed = False # track the state
modes = 0
fadeValue = 0
fadeToggle = False
startTime = time.monotonic()
interval = 0.01
increase = 5
currentColor = -1
intervall = 0.1
changer = False
red = (255, 0, 0)
blue = (0, 0, 255)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1, auto_write=False)

def on():
    global startTime
    global intervall
    global currentColor

    if time.monotonic()-startTime > intervall:
        startTime = time.monotonic()
        currentColor = currentColor + 1
        if currentColor >= len(red):
            currentColor = -1
        pixels.fill(blue)
        pixels.show()
def getValue():
    global fadeValue
    global fadeToggle
    global startTime
    global interval
    global increase
    now = time.monotonic()
    #print("current time:" + str(now))
    if now - startTime > interval:
        startTime = time.monotonic()
        #print("current time:" + str(now))
        # fadeValue is greater than or equal to 255
        if(fadeValue >= 255):
            fadeToggle = True
        # fadeValue is less than or equal to 0
        if(fadeValue <= 0):
            fadeToggle = False

        if(fadeToggle == False):
            fadeValue = fadeValue+increase

        if(fadeToggle == True):
            fadeValue = fadeValue-increase

        if(fadeValue == 0):
            changer == False



def animation1():
    global fadeValue
    global fadeToggle
    global startTime
    global interval
    global increase
    now = time.monotonic()
    #print("current time:" + str(now))
    if now - startTime > interval:
        startTime = time.monotonic()
        #print("current time:" + str(now))
        # fadeValue is greater than or equal to 255
        if(fadeValue >= 255):
            fadeToggle = True

        # fadeValue is less than or equal to 0

        if(fadeValue <= 0):
            fadeToggle = False


        if(fadeToggle == False):
            fadeValue = fadeValue+increase

        if(fadeToggle == True):
            fadeValue = fadeValue-increase

    for neoPixelNum in range(len(pixels)):
        pixels[neoPixelNum] = (0,0,fadeValue)
        pixels.show()
def blueBreath():
    for neoPixelNum in range(len(pixels)):
        pixels[neoPixelNum] = (0,0,fadeValue)
        pixels.show()
def redBreath():
    for neoPixelNum in range(len(pixels)):
        pixels[neoPixelNum] = (fadeValue,0,0)
        pixels.show()

while True:
    # str() converts variable output into string
    # When adding string + string you get a sentence
    # string + number, string + bool, string + variable wont work
    # print("Current switch value: " + str(switch.value))
    if switch.value == True:
        # pressed
        led.value = False
        ispressed = True # keeps track that the button was pressed at some time
    else:
        # released
        led.value = True
        if ispressed == True:
            # did the user press the button at any point in time
            print("Clicked")
            ispressed = False # we want to reset the click action
            modes = modes + 1
            print("current mode:" + str(modes))
    if modes == 0:
        print("Mode 0: off")
        # pixels off code
        pixels.fill((0,0,0))
        pixels.show()

    elif modes == 1:
        print("Mode 1: red-war")
        # pixels on code
        '''
        for i in range(4):
            pixels[i] = red
            pixels.show()
        for i in range(5,9):
            pixels[i] = blue
            pixels.show()
        '''
        pixels.fill(red) #two ways to set color
        pixels.show()

    elif modes == 2:
        print("Mode 2: blue-contented")
        # pixels animation code
        #animation1()
        pixels.fill(blue) #two ways to set color
        pixels.show()
    elif modes == 3:
        getValue()
        print(changer)
        if(fadeToggle == True and changer != True): #wrong
            blueBreath()
        else:
            redBreath()

    else:
        modes = 0
    time.sleep(0.01)  # debounce delay


