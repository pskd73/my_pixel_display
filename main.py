from slide import TimeSlide, BhuviBirthdaySlide, IndiaTopNewsSlide
from matrix_display import MatrixDisplay
import time


INTER_SLIDE_DELAY = 1
		

slides = [
	TimeSlide(),
	BhuviBirthdaySlide(),
	IndiaTopNewsSlide()
]


display = MatrixDisplay()
while True:
	for slide in slides:
		slide.show(display)
		time.sleep(INTER_SLIDE_DELAY)

