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
	'cookie':'D_HID=C99D9940-905B-3642-8DF2-41DD387F94FB; D_IID=29722909-8207-351A-A773-7E7F554BDD07; D_UID=0B7876F0-F4C7-36F9-9D0F-05C32EFE0349; D_ZID=032CD097-5A16-3C10-A05A-30124390DB11; D_ZUID=6D9D0A42-4D9A-3EC7-8323-1AC3D65EC781; se_lsa=2018-11-29+18%3A58%3A02+-0500; __CG=u%3A513889454195585000%2Cs%3A432203449%2Ct%3A1543535881986%2Cc%3A35%2Ck%3Astreeteasy.com%2F41%2F41%2F340%2Cf%3A0%2Ci%3A0; _ga=GA1.2.1241560260.1538074790; _gac_UA-122241-1=1.1543517033.EAIaIQobChMIrPaxgaH63gIVjIuzCh3tGAsMEAAYASAAEgJjPvD_BwE; _mkto_trk=id:324-WZA-498&token:_mch-streeteasy.com-1538074791002-36655; _mibhv=anon-1538074790752-1775580676_6815; ki_r=; ki_t=1538074791757%3B1543517033196%3B1543535881918%3B3%3B57; se%3Asearch%3Asales%3Astate=%7C%7C%7C%7C; se%3Asearch%3Ashared%3Astate=100%7C%7C%7C%7Cfalse; _ses=BAh7DEkiD3Nlc3Npb25faWQGOgZFVEkiJTAyMmRjNGNiYmQwMTVlNzA2YTQwOGI1NTRhNjg1MmU1BjsAVEkiDnVzZXJfZGF0YQY7AEZ7EDoQc2FsZXNfb3JkZXJJIg9wcmljZV9kZXNjBjsAVDoScmVudGFsc19vcmRlckkiD3ByaWNlX2Rlc2MGOwBUOhBpbl9jb250cmFjdEY6DWhpZGVfbWFwRjoSc2hvd19saXN0aW5nc0Y6Em1vcnRnYWdlX3Rlcm1pIzoZbW9ydGdhZ2VfZG93bnBheW1lbnRpGTohbW9ydGdhZ2VfZG93bnBheW1lbnRfZG9sbGFyc2kCUMM6Em1vcnRnYWdlX3JhdGVmCTQuNTg6E2xpc3RpbmdzX29yZGVySSIQbGlzdGVkX2Rlc2MGOwBUOhBzZWFyY2hfdmlld0kiDGRldGFpbHMGOwBUSSISbG9va19hbmRfZmVlbAY7AEZJIgkyMDE0BjsAVEkiEWxhc3Rfc2VjdGlvbgY7AEZJIgpzYWxlcwY7AFRJIhBfY3NyZl90b2tlbgY7AEZJIjF3YnNodVplenZlNHp0c29UeXpiVE1wZlg0NEdwMjJ6WDQ1NDVQSHgwc3gwPQY7AEZJIghwaXMGOwBGaTtJIhBsYXN0X3NlYXJjaAY7AEZpArUB--dcbd26d658e14cb31ddccd76ac48eebef39ee213; anon_searcher_stage=initial; se%3Abig_banner%3Asearch=%7B%22437%22%3A2%7D; se_login_trigger=4; last_search_tab=sales; se_rs=437; canadian=false; _gcl_aw=GCL.1543517032.EAIaIQobChMIrPaxgaH63gIVjIuzCh3tGAsMEAAYASAAEgJjPvD_BwE; ken_gclid=EAIaIQobChMIrPaxgaH63gIVjIuzCh3tGAsMEAAYASAAEgJjPvD_BwE; D_SID=160.39.132.26:CVl2d7HgsZ7mUpg5Fmi6aECyw8cGHGLiDkp2AATZaSo; __gads=ID=3b7e608620cc4884:T=1538074790:S=ALNI_MblgW2J73pTKhO32ffbxxdPVOkopQ; _gcl_au=1.1.1971410806.1538074790; _se_t=85494fd9-86fb-474a-bc94-a7ccccb5157c; streeteasy_site=nyc',
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

for i in range(1,500): #ALERT!!! This represents we will scrawl page 12-16. Manually adjust it after changing the cookie
	print("crawling no."+str(i)+' page')
	get_page(i)
	time.sleep(5)

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