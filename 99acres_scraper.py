# Vadodara pagination 715 Residential projects

import requests, bs4
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

root_url = "https://www.99acres.com/new-projects-in-west-bengal-ffid?np_search_type=NL"
html = requests.get(root_url, headers=headers)
soup = bs4.BeautifulSoup(html.text, 'html.parser')

# Pagination
paging = soup.find("div", {"class": "component__pgdiv"}).find_all("a")
# print(paging)

start_page = paging[0].text
last_page = paging[len(paging) - 2].text

# print(start_page)
# print(last_page)

# Write to CSV file
outfile = open('west-bengal Residentialsssss.csv', 'w', encoding="utf-8")
writer = csv.writer(outfile)
writer.writerow(['Site_Name', 'Type', 'Possession', 'Price', 'PricePerSqFt'])

# Scrape per page
pages = list(range(1, int(last_page) + 1))
print(pages)

for page in pages:
    #     url = 'https://www.lookup.pk/dynamic/search.aspx?searchtype=kl&k=gym&l=lahore&page=%s' %(page)
    #     url='https://www.99acres.com/new-projects-in-ahmedabad-ffid-page-'+str(page)+'-?sortby=default&noxid=Y&np_search_type=2028,2027,2026,2025,2024,2023,2022,2021,2020,NL,UC'
    url = 'https://www.99acres.com/new-projects-in-west-bengal-ffid-page-' + str(page) + '?np_search_type=NL'
    print(url)
    html = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    #     print(soup)
    #     print(soup.prettify())
    #     print ('Processing page: %s' %(page))

    #     product_name_list = soup.findAll('div',attrs={'class': 'NpsrpTuple__tableWrap'})
    #     print(product_name_list)
    for article in soup.find_all('div',
                                 attrs={'class': 'NpsrpTuple__tableWrap'}):
        Site_Name = article.td.text
        print(Site_Name)

        Type = article.find('tr', attrs={'class': 'NpsrpTuple__subHead'}).text
        print(Type)

        Possession = article.div.text
        print(Possession)

        try:
            Price = article.find_all('span', attrs={'class': 'NpsrpTuple__webRupee'})[1].text
            print(Price)
        except:
            Price = "No Data"
        #             print('None')

        try:
            PricePerSqFt = article.find_all('span', attrs={'class': 'NpsrpTuple__webRupee'})[0].text
        except:
            PricePerSqFt = "No Data"
        #             print('None')

        writer.writerow([Site_Name, Type, Possession, Price, PricePerSqFt])
outfile.close()
print('Done')