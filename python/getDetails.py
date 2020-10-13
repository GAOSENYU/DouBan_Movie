#!/usr/bin/env python
# coding:utf8

'''
	根据电影id获取详细信息
	
'''

import urllib.request
import json
import time
import random
from bs4 import BeautifulSoup


inputFile = 'douban_movie.txt'
fr = open(inputFile, 'r')
outputFile = 'douban_movie_detail.txt'
fw = open(outputFile, 'w',encoding='utf-8')
fw.write('id^title^url^cover^rate^director^composer^actor^category^district^language^showtime^length\n')

headers = {}
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
# headers["Accept-Encoding"] = "gzip, deflate, sdch"
headers["Accept-Language"] = "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
# headers["Cookie"] = 'bid=JBNDFs4Ov5M; douban-fav-remind=1; __gads=ID=cb848af15dcc4104:T=1582364597:S=ALNI_Mbi3oGs4-czaPvUvNjk-Nq_luk_vg; ll="118232"; _vwo_uuid_v2=D99C37C9CCAE8A8B5BAAAE473538F4283|e582202e09ceaf9b8b2f9fbb13cddcb0; __utmc=30149280; push_doumail_num=0; push_noty_num=4; dbcl2="179598438:M/yLSP30LG0"; ck=HscZ; __utma=30149280.2106565030.1582364600.1587379852.1587382144.11; __utmb=30149280.0.10.1587382144; __utmz=30149280.1587382144.11.10.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login'
headers["Host"] = "movie.douban.com"
headers["Referer"] = "http://movie.douban.com/"
headers["Upgrade-Insecure-Requests"] = 1
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

firstLine = True

count = 1

errorCount = 0

result = {}

for line in fr:
	if firstLine:
		firstLine = False
		continue

	line = line.split(';')

	movieId = line[0]
	title = line[1]
	url = line[2]
	cover = line[3]
	rate = line[4].rstrip('\n')

	if movieId in result:
		continue
	else:
		result[str(movieId)] = 1

	try:
		request = urllib.request.Request(url=url,headers=headers)
		response = urllib.request.urlopen(request,timeout=10)
		html = response.read()
		html = BeautifulSoup(html,'lxml')

		info = html.select('#info')[0]
		info = info.get_text().split('\n')

		# 提取字段，只要冒号后面的文本内容
		director = info[1].split(':')[-1].strip()
		composer = info[2].split(':')[-1].strip()
		actor = info[3].split(':')[-1].strip()
		category = info[4].split(':')[-1].strip()
		district = info[5].split(':')[-1].strip()
		language = info[6].split(':')[-1].strip()
		showtime = info[7].split(':')[-1].strip()
		length = info[8].split(':')[-1].strip()
		othername = info[9].split(':')[-1].strip()

		# # 电影简ç介
		# description = html.find_all("span", attrs={"property": "v:summary"})[0].get_text()
		# description = description.lstrip().lstrip('\n\t').rstrip().rstrip('\n\t').replace('\n','\t')

		# 写入数据
		record = str(movieId) + '^' + title + '^' + url + '^' + cover + '^' + str(rate) + '^' + director + '^' + composer + '^' + actor + '^' + category + '^' + district+ '^' + language+ '^' + showtime+ '^' + length +'^'+ othername +'\n'
		fw.write(record)
		print (count,title)
		time.sleep(0.5)
	
	except Exception as e:
		print (e)
		print (count,title,"Error")
		errorCount = errorCount + 1
	else:
		pass
	finally:
		pass

	count = count + 1
	
print (count, errorCount)
fr.close()
fw.close()