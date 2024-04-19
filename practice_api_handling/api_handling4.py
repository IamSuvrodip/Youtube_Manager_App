import requests

baseurl = "https://api.freeapi.app/api/v1/public/stocks/stock/random"

r = requests.get(baseurl)
data = r.json()

name = data['data']['Name']
Symbol = data['data']['Symbol']
ListingDate = data['data']['ListingDate']
ISIN = data['data']['ISIN']
MarketCap = data['data']['MarketCap']
CurrentPrice = data['data']['CurrentPrice']
HighLow = data['data']['HighLow']
StockPE = data['data']['StockPE']
BookValue = data['data']['BookValue']
print(f"\nName:{name}\nSymbol:{Symbol}\nListingDate:{ListingDate}\nISIN:{ISIN}\nMarketCap:{MarketCap}\nCurrentPrice:{CurrentPrice}\nHighLow:{HighLow}\nStockPE:{StockPE}\nStockPE:{StockPE}\nBookValue:{BookValue}")