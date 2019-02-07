# coding: utf-8

import os

import fetcher
import extractor

def get_search_data(query, page_num, file_prename):
	for pn in range(1, page_num + 1):
		#print pn
		html = fetcher.get_search_page(query, pn)
		f = open('%s%d.html' % (file_prename, pn), 'wb+')
		f.write(html)
		f.close()
	pass

def extract_search_data(page_num, file_prename):
	search_data = []
	for pn in range(1, page_num + 1):
		f = open('%s%d.html' % (file_prename, pn), 'r')
		res = extractor.extract_search_result(f.read())
		search_data.extend(res)
		f.close()
	return search_data

def get_link_data(valid_link, link_file_prename):
	f = open('%surl_list.html' % link_file_prename, 'wb+')
	for url in valid_link:
		f.write(url + '\n')
	f.close()
	for num in range(0, len(valid_link)):
		url = valid_link[num]
		print url
		html = fetcher.get_page(url)
		f = open('%s%d.html' % (link_file_prename, num + 1), 'wb+')
		f.write(html)
		f.close()
	pass

def ana_file(path):
	f = open(path, 'r')
	res = extractor.extract_file(f.read())
	print path
	f.close()
	return res

def ana_data(link_file_prename):
	file_list = os.listdir(link_file_prename)
	for i in range(0, len(file_list)):
		path = os.path.join(link_file_prename, file_list[i])
		if os.path.getsize(path) < 1024:
			continue
		if os.path.isfile(path):
			ana_file(path)
		break
	pass

def crawl_data():
	query = '华为手机 mate 20'
	page_num = 10
	search_file_prename = 'search_data/'
	#get_search_data(query, page_num, search_file_prename)
	search_data = extract_search_data(page_num, search_file_prename)
	valid_link = extractor.get_valid_link(query, search_data)
	link_file_prename = 'link_data/'
	get_link_data(valid_link, link_file_prename)

def test():
	link_file_prename = 'link_data/'
	ana_data(link_file_prename)
	pass

if __name__ == '__main__':
	#crawl_data()
	test()
	pass

