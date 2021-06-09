from matrix_display import MatrixDisplay
from abc import abstractmethod
from datetime import datetime
import requests
import reader


def text_to_width(text: str):
	return len(text)//5 + 1


class Slide:
	@abstractmethod
	def show(self, display: MatrixDisplay):
		pass
		

class TimeSlide(Slide):
	def show(self, display: MatrixDisplay):
		now = datetime.now()
		display.hero_entry(now.strftime('%H:%M'), x_offset=4)


class BhuviBirthdaySlide(Slide):
	def show(self, display: MatrixDisplay):
		birthday = datetime(2021, 7, 31)
		now = datetime.now()
		display.marquee('Bhuvi\'s birthday {} days to go'.format((birthday - now).days), 8, delay=0.01)


class IndiaTopNewsSlide(Slide):
	def __init__(self):
		self.reader = reader.make_reader('db.sqlite')
		try:
			self.reader.add_feed('https://www.indiatoday.in/rss/1206584')
		except reader.exceptions.FeedExistsError:
			pass
		self.reader.update_feeds()
		self.times_showed = 1
	
	def show(self, display: MatrixDisplay):
		if self.times_showed % 5 == 0:
			self.reader.update_feeds()
		top_5_titles = ' --- '.join([e.title for e in list(self.reader.get_entries())[:5]])
		text_to_show = 'Top news - ' + top_5_titles
		display.marquee(text_to_show, text_to_width(text_to_show), delay=0.01)
		

class QuotableSlide(Slide):
	def show(self, display: MatrixDisplay):
		res = requests.get('https://api.quotable.io/random?tags=technology,famous-quotes').json()
		quote_text = 'Quote - ' + res['content']
		display.marquee(quote_text, text_to_width(quote_text), delay=0.01)
		
