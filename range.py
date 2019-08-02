import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
word = response.content.splitlines()
some_word = random.choice(word).decode('utf-8')
