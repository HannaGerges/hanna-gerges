import requests
import bs4
url=("https://www.ashford.com/sale/glycine.html")
result = requests.get(url)
soup = bs4.BeautifulSoup(result.content ,"html.parser")
inf = soup.find_all('div',{'class':'product details product-item-details'})

for item in inf:
    print(item.find('a',{'class':'product-item-link'}).text)
    print(item.find('div', {'class': 'price-box price-final_price'}).text)
    print()
