from ip2geotools.databases.noncommercial import DbIpCity
ip = '91.193.179.190'
response = DbIpCity.get(ip, api_key='free')
print(response.country)
print(response.region)
print(response.city)
print(response.latitude)
print(response.longitude)
