import requests

# url = 'https://data.openupstate.org/rest/organizations?org_status=active&_format=json'
# r = requests.get(url)
# print(r.json())


r = requests.get('https://api.meetup.com/{}/events?&sign=true&no_earlier_than=2020-03-31T00:00:00.000&no_later_than=2021-03-31T00:00:00.000&photo-host=public&page=50'.format('synergymill'))
print(r.json())