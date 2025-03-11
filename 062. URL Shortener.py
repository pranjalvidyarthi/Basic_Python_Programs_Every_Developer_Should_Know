# URL Shortener using python
import pyshorteners
s = pyshorteners.Shortener()
short_url = s.tinyurl.short('www.youtube.com/@pranjaltechnology')

print('Shortened URL: ' , short_url)