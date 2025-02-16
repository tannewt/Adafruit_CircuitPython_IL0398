"""Simple test script for 4.2" 400x300 tri-color displays.

Supported products:
  * WaveShare 4.2" Color
    * https://www.waveshare.com/product/modules/oleds-lcds/e-paper/4.2inch-e-paper-b.htm
    * https://www.waveshare.com/product/modules/oleds-lcds/e-paper/4.2inch-e-paper-c.htm
    * https://www.waveshare.com/product/modules/oleds-lcds/e-paper/4.2inch-e-paper-module-c.htm
    * https://www.waveshare.com/product/modules/oleds-lcds/e-paper/4.2inch-e-paper-module-b.htm
  """

import time
import board
import busio
import displayio
import adafruit_il0398

displayio.release_displays()

# This pinout works on a Metro and may need to be altered for other boards.
# For breadboarding
spi = busio.SPI(board.SCL, board.SDA)
epd_cs = board.D9
epd_dc = board.D8
epd_reset = board.D7
epd_busy = board.D6

display_bus = displayio.FourWire(spi, command=epd_dc, chip_select=epd_cs, reset=epd_reset,
                                 baudrate=1000000)
time.sleep(1)

display = adafruit_il0398.IL0398(display_bus, width=400, height=300, seconds_per_frame=20,
                                 highlight_color=0xff0000, busy_pin=epd_busy)

g = displayio.Group()

f = open("/display-ruler.bmp", "rb")

pic = displayio.OnDiskBitmap(f)
t = displayio.TileGrid(pic, pixel_shader=displayio.ColorConverter())
g.append(t)

display.show(g)

display.refresh()

time.sleep(120)
