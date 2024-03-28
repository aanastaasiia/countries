from django.shortcuts import render
from django.http import HttpResponse
import requests
import sqlite3
# Create your views here.

connection = sqlite3.connect('countries.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Countries (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
capital TEXT NOT NULL,
subregion TEXT NOT NULL,
region TEXT NOT NULL,
population INTEGER,
area INTEGER,
imezones TEXT NOT NULL,
borders TEXT NOT NULL,
numericCode INTEGER,
flag TEXT NOT NULL           
)
''')
connection.commit()
connection.close()


connection = sqlite3.connect('countries.db')
cursor = connection.cursor()
json = [{"name":"Afghanistan","capital":"Kabul","subregion":"Southern Asia","region":"Asia","population":40218234,"area":652230,"timezones":["UTC+04:30"],"borders":["IRN","PAK","TKM","UZB","TJK","CHN"],"numericCode":"004","flag":"https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_the_Taliban.svg"},{"name":"Åland Islands","capital":"Mariehamn","subregion":"Northern Europe","region":"Europe","population":28875,"area":1580,"timezones":["UTC+02:00"],"borders":"[]","numericCode":"248","flag":"https://flagcdn.com/ax.svg"},{"name":"Albania","capital":"Tirana","subregion":"Southern Europe","region":"Europe","population":2837743,"area":28748,"timezones":["UTC+01:00"],"borders":["MNE","GRC","MKD","UNK"],"numericCode":"008","flag":"https://flagcdn.com/al.svg"},{"name":"Algeria","capital":"Algiers","subregion":"Northern Africa","region":"Africa","population":44700000,"area":2381741,"timezones":["UTC+01:00"],"borders":["TUN","LBY","NER","ESH","MRT","MLI","MAR"],"numericCode":"012","flag":"https://flagcdn.com/dz.svg"},{"name":"American Samoa","capital":"Pago Pago","subregion":"Polynesia","region":"Oceania","population":55197,"area":199,"timezones":["UTC-11:00"],"borders":"[]","numericCode":"016","flag":"https://flagcdn.com/as.svg"},{"name":"Andorra","capital":"Andorra la Vella","subregion":"Southern Europe","region":"Europe","population":77265,"area":468,"timezones":["UTC+01:00"],"borders":["FRA","ESP"],"numericCode":"020","flag":"https://flagcdn.com/ad.svg"},{"name":"Angola","capital":"Luanda","subregion":"Middle Africa","region":"Africa","population":32866268,"area":1246700,"timezones":["UTC+01:00"],"borders":["COG","COD","ZMB","NAM"],"numericCode":"024","flag":"https://flagcdn.com/ao.svg"},{"name":"Anguilla","capital":"The Valley","subregion":"Caribbean","region":"Americas","population":13452,"area":91,"timezones":["UTC-04:00"],"borders":"[]","numericCode":"660","flag":"https://flagcdn.com/ai.svg"},{"name":"Antarctica","capital":"[]","subregion":"Antarctica","region":"Polar","population":1000,"area":14000000,"timezones":["UTC-03:00","UTC+03:00","UTC+05:00","UTC+06:00","UTC+07:00","UTC+08:00","UTC+10:00","UTC+12:00"],"borders":"[]","numericCode":"010","flag":"https://flagcdn.com/aq.svg"},{"name":"Antigua and Barbuda","capital":"Saint John's","subregion":"Caribbean","region":"Americas","population":97928,"area":442,"timezones":["UTC-04:00"],"borders":"[]","numericCode":"028","flag":"https://flagcdn.com/ag.svg"},{"name":"Argentina","capital":"Buenos Aires","subregion":"South America","region":"Americas","population":45376763,"area":2780400,"timezones":["UTC-03:00"],"borders":["BOL","BRA","CHL","PRY","URY"],"numericCode":"032","flag":"https://flagcdn.com/ar.svg"},{"name":"Armenia","capital":"Yerevan","subregion":"Western Asia","region":"Asia","population":2963234,"area":29743,"timezones":["UTC+04:00"],"borders":["AZE","GEO","IRN","TUR"],"numericCode":"051","flag":"https://flagcdn.com/am.svg"},{"name":"Aruba","capital":"Oranjestad","subregion":"Caribbean","region":"Americas","population":106766,"area":180,"timezones":["UTC-04:00"],"borders":"[]","numericCode":"533","flag":"https://flagcdn.com/aw.svg"},{"name":"Australia","capital":"Canberra","subregion":"Australia and New Zealand","region":"Oceania","population":25687041,"area":7692024,"timezones":["UTC+05:00","UTC+06:30","UTC+07:00","UTC+08:00","UTC+09:30","UTC+10:00","UTC+10:30","UTC+11:30"],"borders":"[]","numericCode":"036","flag":"https://flagcdn.com/au.svg"},{"name":"Austria","capital":"Vienna","subregion":"Central Europe","region":"Europe","population":8917205,"area":83871,"timezones":["UTC+01:00"],"borders":["CZE","DEU","HUN","ITA","LIE","SVK","SVN","CHE"],"numericCode":"040","flag":"https://flagcdn.com/at.svg"},{"name":"Azerbaijan","capital":"Baku","subregion":"Western Asia","region":"Asia","population":10110116,"area":86600,"timezones":["UTC+04:00"],"borders":["ARM","GEO","IRN","RUS","TUR"],"numericCode":"031","flag":"https://flagcdn.com/az.svg"},{"name":"Bahamas","capital":"Nassau","subregion":"Caribbean","region":"Americas","population":393248,"area":13943,"timezones":["UTC-05:00"],"borders":"[]","numericCode":"044","flag":"https://flagcdn.com/bs.svg"},{"name":"Bahrain","capital":"Manama","subregion":"Western Asia","region":"Asia","population":1701583,"area":765,"timezones":["UTC+03:00"],"borders":"[]","numericCode":"048","flag":"https://flagcdn.com/bh.svg"},{"name":"Bangladesh","capital":"Dhaka","subregion":"Southern Asia","region":"Asia","population":164689383,"area":147570,"timezones":["UTC+06:00"],"borders":["MMR","IND"],"numericCode":"050","flag":"https://flagcdn.com/bd.svg"},{"name":"Barbados","capital":"Bridgetown","subregion":"Caribbean","region":"Americas","population":287371,"area":430,"timezones":["UTC-04:00"],"borders":"[]","numericCode":"052","flag":"https://flagcdn.com/bb.svg"},{"name":"Belarus","capital":"Minsk","subregion":"Eastern Europe","region":"Europe","population":9398861,"area":207600,"timezones":["UTC+03:00"],"borders":["LVA","LTU","POL","RUS","UKR"],"numericCode":"112","flag":"https://flagcdn.com/by.svg"},{"name":"Belgium","capital":"Brussels","subregion":"Western Europe","region":"Europe","population":11555997,"area":30528,"timezones":["UTC+01:00"],"borders":["FRA","DEU","LUX","NLD"],"numericCode":"056","flag":"https://flagcdn.com/be.svg"},{"name":"Belize","capital":"Belmopan","subregion":"Central America","region":"Americas","population":397621,"area":22966,"timezones":["UTC-06:00"],"borders":["GTM","MEX"],"numericCode":"084","flag":"https://flagcdn.com/bz.svg"},{"name":"Benin","capital":"Porto-Novo","subregion":"Western Africa","region":"Africa","population":12123198,"area":112622,"timezones":["UTC+01:00"],"borders":["BFA","NER","NGA","TGO"],"numericCode":"204","flag":"https://flagcdn.com/bj.svg"},{"name":"Bermuda","capital":"Hamilton","subregion":"Northern America","region":"Americas","population":63903,"area":54,"timezones":["UTC-04:00"],"borders":"[]","numericCode":"060","flag":"https://flagcdn.com/bm.svg"},{"name":"Bhutan","capital":"Thimphu","subregion":"Southern Asia","region":"Asia","population":771612,"area":38394,"timezones":["UTC+06:00"],"borders":["CHN","IND"],"numericCode":"064","flag":"https://flagcdn.com/bt.svg"},{"name":"Bolivia (Plurinational State of)","capital":"Sucre","subregion":"South America","region":"Americas","population":11673029,"area":1098581,"timezones":["UTC-04:00"],"borders":["ARG","BRA","CHL","PRY","PER"],"numericCode":"068","flag":"https://flagcdn.com/bo.svg"},{"name":"Bonaire, Sint Eustatius and Saba","capital":"Kralendijk","subregion":"Caribbean","region":"Americas","population":17408,"area":294,"timezones":["UTC-04:00"],"borders":"[]","numericCode":"535","flag":"https://flagcdn.com/bq.svg"},{"name":"Bosnia and Herzegovina","capital":"Sarajevo","subregion":"Southern Europe","region":"Europe","population":3280815,"area":51209,"timezones":["UTC+01:00"],"borders":["HRV","MNE","SRB"],"numericCode":"070","flag":"https://flagcdn.com/ba.svg"},{"name":"Botswana","capital":"Gaborone","subregion":"Southern Africa","region":"Africa","population":2351625,"area":582000,"timezones":["UTC+02:00"],"borders":["NAM","ZAF","ZMB","ZWE"],"numericCode":"072","flag":"https://flagcdn.com/bw.svg"}]
for i in json:
    cursor.execute('INSERT INTO Countries (name, capital, subregion, region, population, area, imezones, borders, numericCode, flag) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (i['name'], i['capital'], i['region'], i['subregion'], i['population'], i['area'], ', '.join(i['timezones']), ', '.join(i['borders']), i['numericCode'], i['flag']))
connection.commit()
connection.close()


connection = sqlite3.connect('countries.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Countries')
s = cursor.fetchall()

connection.commit()
connection.close()


connection = sqlite3.connect('countries.db', check_same_thread=False)
cursor = connection.cursor()
def index(request):
    page = request.GET.get('page', 1)
    filtr = request.GET.get('filter', 'asc')
    return render(request=request, template_name='index.html')

def country(request):
    coun = request.GET.get('id', 1)
    if request.method == 'GET':
        cursor.execute('SELECT * FROM Countries WHERE id = ?', (coun,))
        context = {'context': cursor.fetchall()}
        return render(request=request, template_name='country.html', context=context)

