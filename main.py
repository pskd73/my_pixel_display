from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from PIL import ImageFont
import time

BOARD_WIDTH = 32
BOARD_HEIGHT = 8


class MatrixDisplay:
	def __init__(self):
		self.serial = spi(port=0, device=0, gpio=noop())
		self.device = max7219(
			self.serial, 
			cascaded=4, 
			block_orientation=90, 
			blocks_arranged_in_reverse_order=True
		)
		self.font = ImageFont.truetype('./pixelmix.ttf', 8)

	def marquee(self, text: str, width: int):
		viewport_width = BOARD_WIDTH * width
		self.virtual = viewport(
			self.device, 
			width=viewport_width, 
			height=BOARD_HEIGHT
		)
		with canvas(self.virtual) as draw:
			draw.text((BOARD_WIDTH, 0), text, fill='white', font=self.font)
		offset = 0
		while offset < viewport_width - BOARD_WIDTH:
			self.virtual.set_position((offset, 0))
			offset += 1
			time.sleep(0.1)


display = MatrixDisplay()
i = 0
while True:
	display.marquee(f'{i} - Hello Bhuvi', 5)
	i += 1
