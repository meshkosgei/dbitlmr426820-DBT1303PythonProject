# set up PiCamera
camera = picamera.PiCamera()
camera.resolution = (320, 240)
 
# set up door sensor
door_sensor = digitalio.DigitalInOut(D5)
door_sensor.direction = digitalio.Direction.INPUT
 
# set up motion sensor
pir_sensor = digitalio.DigitalInOut(D6)
pir_sensor.direction = digitalio.Direction.INPUT
prev_pir_value = pir_sensor.value
is_pir_activated = False
 
# set up sgp30
i2c_bus = I2C(SCL, SDA, frequency=100000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c_bus)
 
# set up the neopixel strip
pixels = neopixel.NeoPixel(D18, NUM_PIXELS_STRIP)
pixels.fill((0, 0, 0))
pixels.show()