# coding: utf-8

import HTMLParser
import sys
import os
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall

from goose import Goose
import goose
from goose.text import StopWordsChinese

reload(sys)
sys.setdefaultencoding('utf-8')

html = ''

tagstack = []
class ShowStructure(HTMLParser.HTMLParser):
	def handle_starttag(self, tag, attrs): tagstack.append(tag)
	def handle_endtag(self, tag): tagstack.pop()
	def handle_data(self, data):
		if data.strip():
			for tag in tagstack: sys.stdout.write('/' + tag)
			sys.stdout.write(' >> %s\n' %s data.strip())

def test(filename = 'link_data/31.html'):
	link_file_prename = './link_data/'
	file_list = os.listdir(link_file_prename)
	for i in range(0, len(file_list)):
		path = os.path.join(link_file_prename, file_list[i])
		if os.path.getsize(path) < 1024:
			continue
		if os.path.isfile(path):
			ana_file(path)

def ana_file(filename):
	print filename
	f = open(filename, mode='r')
	#g = goose.Goose()
	g = Goose({'stopwords_class': StopWordsChinese})
	article = g.extract(raw_html = f.read())
	print article.title
	print article.meta_description
	print article.cleaned_text
	'''
	print article.meta_description
	print article.meta_keywords
	print article.tags
	print article.top_image
	print article.infos
	'''
	f.close()

if __name__ == '__main__':
	test()

