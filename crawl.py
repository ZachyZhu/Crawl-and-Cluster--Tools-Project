import pandas as pd
import requests
import time
from lxml import etree
from bs4 import BeautifulSoup

headers = { #creat headers for crawl
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9',
	'ra-sid': '5b6efc004ffa04af848017f1',
	# your cookies: ALERT!!! we have to change cookie after crawling 4 pages because streeteasy has some anti-crawl measures.
	'cookie':'D_SID=98.15.81.209:pOszsfmuR0rVeBOq5wIl+YwIuYllFS8dxupCNRFu0IQ; streeteasy_site=nyc; _se_t=21336211-ed0e-40f2-a840-f61cc7fdb7a7; _gcl_aw=GCL.1543199679.EAIaIQobChMIp7CM4oLx3gIVgR-GCh32YwQCEAAYASAAEgK4XfD_BwE; _gcl_au=1.1.1125338001.1543199679; __gads=ID=2ed35eb167791b3b:T=1543199679:S=ALNI_MYqtwpvvwpRvsV65q5SFvgTcEVCkg; _ga=GA1.2.1515464739.1543199679; ken_gclid=EAIaIQobChMIp7CM4oLx3gIVgR-GCh32YwQCEAAYASAAEgK4XfD_BwE; _mibhv=anon-1543199680492-7922821982_6815; _gac_UA-122241-1=1.1543199681.EAIaIQobChMIp7CM4oLx3gIVgR-GCh32YwQCEAAYASAAEgK4XfD_BwE; _mkto_trk=id:324-WZA-498&token:_mch-streeteasy.com-1543199680928-85841; ki_r=; D_IID=A076B590-6499-353F-8AC3-DC105D9B61B0; D_UID=C90CEB1B-6CAF-349B-9F23-F63B3B85A4A1; last_search_tab=sales; se_rs=437; se%3Asearch%3Ashared%3Astate=100%7C%7C%7C%7Cfalse; se%3Asearch%3Asales%3Astate=%7C%7C%7C%7C; KruxPixel=true; _gid=GA1.2.1486164932.1543516955; canadian=false; D_ZID=683730B5-CB32-3A40-B229-1E0642CB8A6D; D_ZUID=894F4460-06AC-3290-98BD-95D09DBF769E; D_HID=619CFC35-E67F-3737-9D12-3B9A845A0CBB; _ses=BAh7DEkiD3Nlc3Npb25faWQGOgZFVEkiJWQ3OTExZTYyZmE4ZWI1MGMxZTk0NjYwNDgyNDhhMzE5BjsAVEkiDnVzZXJfZGF0YQY7AEZ7EDoQc2FsZXNfb3JkZXJJIg9wcmljZV9kZXNjBjsAVDoScmVudGFsc19vcmRlckkiD3ByaWNlX2Rlc2MGOwBUOhBpbl9jb250cmFjdEY6DWhpZGVfbWFwRjoSc2hvd19saXN0aW5nc0Y6Em1vcnRnYWdlX3Rlcm1pIzoZbW9ydGdhZ2VfZG93bnBheW1lbnRpGTohbW9ydGdhZ2VfZG93bnBheW1lbnRfZG9sbGFyc2kCUMM6Em1vcnRnYWdlX3JhdGVmCTQuNTg6E2xpc3RpbmdzX29yZGVySSIQbGlzdGVkX2Rlc2MGOwBUOhBzZWFyY2hfdmlld0kiDGRldGFpbHMGOwBUSSISbG9va19hbmRfZmVlbAY7AEZJIgkyMDE0BjsAVEkiEWxhc3Rfc2VjdGlvbgY7AEZJIgpzYWxlcwY7AFRJIhBsYXN0X3NlYXJjaAY7AEZpArUBSSIQX2NzcmZfdG9rZW4GOwBGSSIxWkMvVmhFL1VrYzJGNFlMbW53Z01ueTd4U3BSU0dNUzFCNjJzL2RVd0VyYz0GOwBGSSIIcGlzBjsARmki--9632e3e68bbbb22fd45034c28d6d5654d5493155; ki_t=1543199682123%3B1543516957524%3B1543522930646%3B2%3B30; __CG=u%3A7055923758170329000%2Cs%3A1187949948%2Ct%3A1543522930675%2Cc%3A29%2Ck%3Astreeteasy.com%2F41%2F41%2F340%2Cf%3A0%2Ci%3A0; se_lsa=2018-11-29+15%3A22%3A13+-0500',
	#this cookie has been used. If you want to crawl, change another cookie.
	'connection':'keep-alive',
	'referer': 'https://streeteasy.com/for-sale/manhattan',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
#the same pattern of each page
base_url = "https://streeteasy.com/for-sale/manhattan?page="

#crawl one page
def get_page(page_number):
	response = requests.get(base_url+str(page_number), headers=headers)
	# test whether we get correct status code or not
	if response.status_code == 200:
		text = response.text
		parse_page(text)
	else:
		print('status not 200 error')
		print(response.status_code)

#using etree and beautifulsoup to parse the code
def parse_page(text):
	html_xpath = etree.HTML(text)
	ids = html_xpath.xpath('//article/@id')
	if len(ids) == 0:
		print('error!')
	#the pattern that the attributes all have
	prices = html_xpath.xpath('//article/div[@class="details row"]/ul/li[@class="price-info"]/span[@class="price"]/text()')
	address = html_xpath.xpath('//article/div[@class="details row"]/h3[@class="details-title"]/a/text()')
	types = html_xpath.xpath('//article/div[@class="details row"]/ul/li[@class="details_info"]/text()')
	newtypes = []
	for t in types:
		if '\n' in t:
			newtypes.append(t.strip().split(' ')[0])

	soup = BeautifulSoup(text, 'lxml')
	uls = soup.find_all('ul', attrs={'class': 'details_info details-info-flex'})
	beds = []
	baths = []
	areas = []
	for ul in uls:
		strings = str('')
		for li in ul.find_all('li'):
			strings = strings + li.text

		if 'bed' not in strings:
			beds.append('')
		else:
			for li in ul.find_all('li'):
				if 'bed' in li.text:
					beds.append(li.text)

		if 'bath' not in strings:
			baths.append('')
		else:
			for li in ul.find_all('li'):
				if 'bath' in li.text:
					baths.append(li.text)

		if 'ft' not in strings:
			areas.append('')
		else:
			for li in ul.find_all('li'):
				if 'ft' in li.text:
					areas.append(li.text)

	global id_list
	global price_list
	global address_list
	global types_list
	global bath_list
	global bed_list
	global area_list

	id_list = id_list + ids
	price_list = price_list + prices
	address_list = address_list + address
	types_list = types_list + newtypes
	bed_list = bed_list + beds
	bath_list = bath_list + baths
	area_list = area_list + areas



id_list = []
price_list = []
address_list = []
types_list = []
bed_list = []
bath_list = []
area_list = []

for i in range(12,16): #ALERT!!! This represents we will scrawl page 12-16. Manually adjust it after changing the cookie
	print("crawling no."+str(i)+' page')
	get_page(i)

data = {
	'id': id_list,
	'price': price_list,
	'address': address_list,
	'type': types_list,
	'bed': bed_list,
	'bath': bath_list,
	'area': area_list
}

pd.DataFrame(data).to_csv('datafile4.csv')