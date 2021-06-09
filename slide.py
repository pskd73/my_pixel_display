from matrix_display import MatrixDisplay
from abc import abstractmethod
from datetime import datetime


class Slide:
	@abstractmethod
	def show(self, display: MatrixDisplay):
		pass
		

class TimeSlide(Slide):
	def show(self, display: MatrixDisplay):
		now = datetime.now()
		display.hero_entry(now.strftime('%H:%M'), x_offset=3)


class BhuviBirthdaySlide(Slide):
	def show(self, display: MatrixDisplay):
		birthday = datetime(2021, 7, 31)
		now = datetime.now()
		display.marquee('Bhuvis birthday {} days to go'.format((birthday - now).days), 8)
