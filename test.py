#!/usr/bin/env python
# coding:utf8

import pymysql
import json
import pprint
import urllib.request


# url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch'
# request = urllib.request.Request(url=url)
# response = urllib.request.urlopen(request)
# html = unicode(response.read())
# code_of_html = html.decode('utf-8')
# print(html)

# db = pymysql.connect(host='localhost', user='root', passwd='root', db='douban', port=8889, charset='utf8', cursorclass = pymysql.cursors.DictCursor)
# db.autocommit(True)
# cursor = db.cursor()

# cursor.execute("select rate, district, category, showtime,length,othername from movie")
# movies = cursor.fetchall()

# temp = []
# for item in movies:
# 	if not item['showtime'] == 0 and not item['length'] == 0:
# 		temp.append(item)
# movies = temp
# # movies = json.dumps({"movies": movies})
# pprint.pprint(movies)

# cursor.execute("select * from rate")
# rates = cursor.fetchall()
# temp = {}
# for item in rates:
# 	temp[item['name']] = {}
# 	temp[item['name']]['categories'] = item['categories'].split(',')
# 	temp[item['name']]['rates'] = item['rates'].split(',')
# 	array = []
# 	for i in temp[item['name']]['rates']:
# 	array.append(float(i))
# 	temp[item['name']]['rates'] = array
# rates = temp
# rates = json.dumps({"rates": rates})

# categories = ['剧情','喜剧','惊悚','爱情','动作','悬疑','犯罪','恐怖','科幻','冒险','奇幻','家庭','动画','战争','历史','古装','传记','音乐','同性','武侠','情色','灾难','运动','歌舞','西部','儿童','黑色电影','鬼怪','荒诞']
# districts = ['United States of America','China','Japan','South Korea','United Kingdom','France','Germany','Canada','Italy','Australia','Spain','Thailand','Russia','Belgium','Sweden','Ireland','Czech Republic','Denmark','India','Poland','Switzerland','New Zealand','Austria','Norway','Netherlands','Brazil','Hungary','Slovakia','Mexico','Iran','South Africa','Finland','Turkey','Romania','Luxembourg','Argentina','Iceland','Indonesia','Israel','United Arab Emirates','Malaysia','Georgia','Cuba','Kazakhstan','Estonia','Vietnam','Greece','Lithuania','Chile','Ukraine','Portugal','Bulgaria','Botswana','The Bahamas','Uzbekistan','Algeria','Puerto Rico','Philippines','Mauritania','Morocco','Latvia','Egypt','Myanmar','Tunisia','Peru','Colombia','Tajikistan']
db = pymysql.connect(host='localhost', user='root', passwd='root', db='douban', port=8889, charset='utf8', cursorclass = pymysql.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()
cursor.execute("select * from rate")
rates = cursor.fetchall()
temp = {}
for item in rates:
	temp[item['name']] = {}
	temp[item['name']]['categories'] = item['categories'].split(',')
	temp[item['name']]['rates'] = item['rates'].split(',')
	array = []
	for i in temp[item['name']]['rates']:
		array.append(float(i))
	temp[item['name']]['rates'] = array
rates = temp
rates = json.dumps({"rates": rates})

