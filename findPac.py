import requests
import sys
from bs4 import BeautifulSoup as bs

try:
	if(len(sys.argv) != 2):
		raise IndexError
	else:
		packageName = sys.argv[1]
except IndexError:
	print('Error, usage is: python3 findPac.py packageName')
	exit()

response = requests.get(
    'https://aur.archlinux.org/packages/{}/'.format(packageName)
)

if(response.status_code == 404):
	print("package {} not found on aur.archlinux.org/packages/{}/".format(packageName, packageName))
	exit(0)

soup = bs(response.text, 'html.parser')

table = soup.find('table', id="pkginfo")
link_elements = table.find_all(
    'a', attrs={"class":'copy'}
)

if (len(link_elements) > 1):
	print('multiple links found:\n')

for element in link_elements:
	print(element['href'])
