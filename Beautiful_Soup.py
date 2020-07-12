import bs4
import requests
url = ("https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print(soup.prettify())
#print(soup.get_text())





container = soup.findAll("div", {"class": "_1HmYoV hCUpcT"})
print(len(container))
print(soup.prettify())









import bs4
import requests

url = ("https://reekacrieation.wordpress.com/2018/05/01/rcb-vs-mi-ipl-2018-match-31-preview-mumbai-and-bangalores-fight-for-survival-begins/")
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
#print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.get_text())

for para in soup.find_all('p'):
    print(para.text)

for links in soup.find_all('a'):
    link = links.get('href')
    print(link)
  


