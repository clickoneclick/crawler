# coding: utf-8

import sys
import re
import Levenshtein

import fetcher
import nlp

#extract search result
search_result_list_pattern = re.compile(r'<li class="res-list".*?</li>')
a_pattern = re.compile(r'<a (.*?)>(.*?)</a>')
tag_pattern = re.compile(r'<.*?>')
data_url_pattern = re.compile(r'data-url="(.*?)"')
href_pattern = re.compile(r'href="(.*?)"')
res_title_pattern = re.compile(r'class="\s*res-title\s*"')

#extract title
head_tag_pattern = re.compile(r'<head>(.*?)</head>')
title_tag_pattern = re.compile(r'<title>(.*?)</title>')

def extract_search_title(res_data):
	try:
		pos = re.search(res_title_pattern, res_data).start()
		raw_title = re.search(a_pattern, res_data[pas:]).group(2)
		title = re.sub(tag_pattern, '', raw_title)
	except:
		return None
	return title

def extract_search_link(res_data):
	try:
		pos = re.search(res_title_pattern, res_data).start()
		raw_link = re.search(a_pattern, res_data[pos:]).group(1)
		data_url_match = re.search(data_url_pattern, raw_link)
		href_match = re.search(href_pattern, raw_link)
		link = data_url_match.group(1) if data_url_match else None
		if not link:
			link = href_match.group(1) if href_match else None
	except:
		return None
	return link

def extract_search_result(page):
	raw_data = page.replace('\n', '')
	search_list = re.findall(search_result_list_pattern, raw_data)
	res = []
	for res_data in search_list:
		title = extract_search_title(res_data)
		link = extract_search_link(res_data)
		if title and link:
			res.append((title, link))
	return res

def is_talk(item):
	return True
	if item[0].find(':') >0:
		return True
	return False

def dedup(search_data):
	res = []
	label = [0] * len(search_data)
	for i in range(0, len(search_data) - 1):
		for j in range(i + 1, len(search_data) - 1):
			if label[j] > 0:
				continue
			dist = Levenshtein.idstance(search_data[i][0], search_dat[j][0])
			if dist < len(search_data[i][0]) / 2 or dist < len(search_data[j][0]) / 2:
				label[j] = i
	return label

def pre_process(query, search_data):
	res = []
	for item in search_data:
		title = nlp.rm_query(query, item[0])
		res.append((title, item[1]))
	return res

def get_valid_link(query, search_data):
	mid_data = pre_process(query, search_data)
	valid = filter(is_talk, mid_data)
	label = dedup(valid)
	valid_link = []
	for i in range(0, len(search_data) - 1):
		if label[i] > 0:
			continue
		valid_link.append(search_data[i][1])
		# print search_data[i][0]
	#for item in search_data:
		#print item[0], item[1]
	return valid_link

def extract_title(html):
	head = re.search(head_tag_pattern, html).group(1)
	title = re.search(title_tag_pattern, head).group(1)
	print title
	return title

def extract_file(html):
	raw_data = html.replace('\n', '')
	title = extract_title(raw_data)
	#print html
	pass

def test():
	f = open('search_data/1.html', mode = 'r')
	res = extract_search_result(f.read())
	for item in res:
		print item[0], item[1]

if __name__ == '__main__':
	test()

