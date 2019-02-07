# coding: utf-8

import sys
import re

space_pattern = re.compile(r'\s+')


def seg_query(query):
	mid_data = re.sub(space_pattern, ' ', query)
	return mid_data.split(' ')

def rm_query(query, title):
	word_array = seg_query(query)
	mid_title = title
	for word in word_array:
		mid_title = re.sub(word, '', mid_title)
	return mid_title


def test():
	query = '华为手机 mate 20'
	title = '2018年保值手机大排名！华为mate20仅排第三，第一名当之无愧！'
	print query
	print title
	res = rm_query(query, title)
	print res

if __name__ == '__main__':
	test()

