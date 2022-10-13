from sense_hat import SenseHat
#The function receives a `float` value as an argument representing a temperature in Celsius.
#Depending on the temperature range, the following colors will be displayed on the Sense HAT
s = SenseHat()
blue = (0, 0, 255)
darkblue = (0, 0, 128)
green = (0, 255, 0)
lightgreen = (50, 205, 50)
red = (255, 0, 0)
white = (0, 0, 0)

def displayColorForTemperature():
    temp = s.get_temperature()
    print("Temperature: %s C" % temp)
    for i in range(64):
        if -10 >= temp >= -40:
            s.clear(darkblue)
        if 0 >= temp >= -9:
            s.clear(blue)
        if 15 >= temp >= 1:
            s.clear(lightgreen)
        if 22 >= temp >= 16:
            s.clear(green)
        if temp > 22:
            s.clear(red)
#The function receives an integer value as an argument representing the humidity as a percentage
#Depending on the humidity range, the Sense HAT displays the relative number of blue lines (100% will be all leds sets to blue)

def LedsOnForHumidity():
    humidity = s.humidity
    h = 64 * humidity / 100
    leds = [blue if i < h else white for i in range(64)]

    s.set_pixels(leds)

LedsOnForHumidity()