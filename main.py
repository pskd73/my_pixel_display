from slide import TimeSlide, BhuviBirthdaySlide
from matrix_display import MatrixDisplay
import time


INTER_SLIDE_DELAY = 1
		

slides = [
	TimeSlide(),
	BhuviBirthdaySlide()
]


display = MatrixDisplay()
while True:
	for slide in slides:
		slide.show(display)
		time.sleep(INTER_SLIDE_DELAY)

