#pip install pygeoip

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')
gi.country_name_by_addr('14.139.61.12')

# output : 'Lebanon'

##############################################################

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')
gi.region_by_addr('14.139.61.12')

#output : {'region_code': u'07', 'country_code': 'IN'}

##############################################################

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')
gi.region_by_name('apple.com')

#output : {'region_code': u'CA', 'country_code': 'US'}

##############################################################

import pygeoip

gi = pygeoip.GeoIP(‘GeoLiteCity.dat’)
gi.record_by_addr(‘14.139.61.12’)

"""
output : 

{
'city': u'New Delhi', 'region_code': u'07', 'area_code': 0,
'time_zone': 'Asia/Calcutta', 	'dma_code': 0, 'metro_code': None,
'country_code3': 'IND',  'latitude': 28.599999999999994,
'postal_code': None, 'longitude': 77.19999999999999,
'country_code': 'IN', 'country_name': 'India', 'continent': 'AS'
}

"""

##############################################################

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')
gi.org_by_name('dell.com')

# output : 'Dell Computer Corporation'

##############################################################

#!usr/bin/env python

import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(ip):
	rec = gi.record_by_name(ip)
	city = rec['city']
	country = rec['country_name']
	longitude = rec['longitude']
	lat = rec['latitude']
	print '[+] Address: '  + ip + ' Geo-located '
	print '[+] ' +str(city)+ ', '+str(country)
	print '[+] Latitude: ' +str(lat)+ ', Longitude: '+ str(longitude)

ip = # Enter an IP(in single quotes)
printRecord(ip)