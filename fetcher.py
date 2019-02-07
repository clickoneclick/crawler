# coding: utf-8

import urllib

def get_page(url):
	html = ''
	try:
		res = urllib.urlopen(url)
		html = res.read().decode('utf-8').encode('utf-8', 'ignore')
	except:
		pass
	return html

def get_search_page(query, pn):
	wd = urllib.quote(query)
	url = r'https://www.so.com/s?q=' + wd + '&pn=%d' % pn
	html = get_page(url)
	return html

def get_search_data():
	query = '华为手机 mate 20'
	for pn in range(1, 11):
		print pn
		html = get_search_page(query, pn)
		f = open('search_data/%d.html' % pn, 'wb+')
		f.write(html)
		f.close()
	pass

if __name__ == '__main__':
	get_search_data()
	pass

