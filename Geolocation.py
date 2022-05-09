#requirments
#pip install abstract-python-ip-geolocation


# Get a Geolocation from an IP Address Abstract's IP Geolocation API and Python
from python_ip_geolocation import AbstractIpGeolocation

IP_GEOLOCATION_API_KEY =  "yyyyyy"; # Get your API Key from https://app.abstractapi.com/api/ip-geolocation/documentation

AbstractIpGeolocation.configure(IP_GEOLOCATION_API_KEY)
#print(AbstractIpGeolocation.look_up("52.97.215.98"))#test one

'''
output

ResponseObject(ip_address='52.97.215.98', city='Paris',
city_geoname_id=2988507, region='Île-de-France', region_iso_code='IDF',
region_geoname_id=3012874, postal_code='75001', country='France',
country_code='FR', country_geoname_id=3017382, country_is_eu=True,
continent='Europe', continent_code='EU', continent_geoname_id=6255148,
longitude=2.3281, latitude=48.8607, security=EmbeddedObject(is_vpn=False),
timezone=EmbeddedObject(name='Europe/Paris', abbreviation='CEST',
gmt_offset=2, current_time='18:48:35', is_dst=True),
flag=EmbeddedObject(emoji='🇫🇷', unicode='U+1F1EB U+1F1F7',
png='https://static.abstractapi.com/country-flags/FR_flag.png',
svg='https://static.abstractapi.com/country-flags/FR_flag.svg'),
currency=EmbeddedObject(currency_name='Euros', currency_code='EUR'),
connection=EmbeddedObject(autonomous_system_number=8075,
autonomous_system_organization='MICROSOFT-CORP-MSN-AS-BLOCK',
connection_type='Corporate', isp_name='Microsoft Corporation',
organization_name='Microsoft Corporation'))
'''


#print(AbstractIpGeolocation.look_up("136.243.39.33"))#test two

'''
output

ResponseObject(ip_address='136.243.39.33', city=None, city_geoname_id=None,
region=None, region_iso_code=None, region_geoname_id=None, postal_code=None,
country='Germany', country_code='DE', country_geoname_id=2921044,
country_is_eu=True, continent='Europe', continent_code='EU',
continent_geoname_id=6255148, longitude=9.491, latitude=51.2993,
security=EmbeddedObject(is_vpn=False),
timezone=EmbeddedObject(name='Europe/Berlin', abbreviation='CEST', gmt_offset=2, current_time='18:52:50', is_dst=True),
flag=EmbeddedObject(emoji='🇩🇪', unicode='U+1F1E9 U+1F1EA',
png='https://static.abstractapi.com/country-flags/DE_flag.png',
svg='https://static.abstractapi.com/country-flags/DE_flag.svg'),
currency=EmbeddedObject(currency_name='Euros', currency_code='EUR'),
connection=EmbeddedObject(autonomous_system_number=24940,
autonomous_system_organization='Hetzner Online GmbH',
connection_type='Corporate', isp_name='Hetzner Online GmbH',
organization_name='Hetzner'))
'''

#print(AbstractIpGeolocation.look_up("192.168.0.104"))#test three private no data

'''
output

ResponseObject(ip_address='192.168.0.104', city=None, city_geoname_id=None,
region=None, region_iso_code=None, region_geoname_id=None, postal_code=None,
country=None, country_code=None, country_geoname_id=None, country_is_eu=None,
continent=None, continent_code=None, continent_geoname_id=None, longitude=None,
latitude=None, security=EmbeddedObject(is_vpn=False))
'''

print(AbstractIpGeolocation.look_up("35.174.127.31"))

'''
output

ResponseObject(ip_address='35.174.127.31', city=None, city_geoname_id=None,
region=None, region_iso_code=None, region_geoname_id=None, postal_code=None,
country='United States', country_code='US', country_geoname_id=6252001,
country_is_eu=False, continent='North America', continent_code='NA',
continent_geoname_id=6255149, longitude=-97.822, latitude=37.751,
security=EmbeddedObject(is_vpn=False), timezone=EmbeddedObject(name='America/Chicago',
abbreviation='CDT', gmt_offset=-5, current_time='12:01:34', is_dst=True),
flag=EmbeddedObject(emoji='🇺🇸', unicode='U+1F1FA U+1F1F8',
png='https://static.abstractapi.com/country-flags/US_flag.png',
svg='https://static.abstractapi.com/country-flags/US_flag.svg'),
currency=EmbeddedObject(currency_name='USD', currency_code='USD'),
connection=EmbeddedObject(autonomous_system_number=14618,
autonomous_system_organization='AMAZON-AES', connection_type='Corporate',
isp_name='Amazon.com, Inc.', organization_name='Amazon Technologies Inc'))
'''