from sense_hat import SenseHat

s = SenseHat()
blue = (0, 0, 255)
darkblue = (0, 0, 128)
green = (0, 255, 0)
lightgreen = (50, 205, 50)
red = (255, 0, 0)
white = (0, 0, 0)


def gettemp():
    temp_input = float(input("Enter temperature in Celsius:"))
    return (temp_input)

def displayColorForTemperature(temp):
    t = round(temp)
    for i in range(64):
        if -10 >= t >= -40:
            s.clear(darkblue)
        if 0 >= t >= -9:
            s.clear(blue)
        if 15 >= t >= 1:
            s.clear(lightgreen)
        if 22 >= t >= 16:
            s.clear(green)
        if t >= 23:
            s.clear(red)
    print("Current temperature: %s C" % t)

temp = gettemp()
displayColorForTemperature(temp)  # call temperature function


def gethum():
    hum_input = int(input("Enter a humidity number:"))
    return (hum_input)

def LedsOnForHumidity(leds):
    h = 64 * leds / 100
    leds = [blue if i < h else white for i in range(64)]
    s.set_pixels(leds)

h = gethum()
LedsOnForHumidity(h)  # call humidity function