import urllib.request
import re

url = "https://finance.naver.com/item/main.naver?code=088980"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

# print(html_contents)

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)",html_contents)

today_stock = stock_results[0]
today_index = today_stock[1]

# print(stock_results)
# print(today_stock)
# print(today_index)

index_list = re.findall("(\<dd\>)([\s\S]+?)(\</dd\>)",today_index)

for index in index_list:
    print(index[1])