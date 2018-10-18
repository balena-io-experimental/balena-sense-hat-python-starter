from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear()
sense.load_image("img/balena.png")
time.sleep(2)
sense.show_message("balena")
sense.clear()
