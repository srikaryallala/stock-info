#Stock Info Finder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#List of stocks to find data for
stocks = ['MSFT','AAPL','GOOG']

#Google URL
URL = 'http://www.google.com'

#Start Headless Chrome Webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def getStockInfo(stock):
    #Navigate to Google
    driver.get(URL)

    #Fill in search bar and press enter for stock info
    driver.find_element_by_name("q").send_keys(stock + Keys.ENTER)

    #Return text in Google "Bubble"
    bubbleData = driver.find_element_by_id("knowledge-finance-wholepage__entity-summary").text
    lines = bubbleData.split('\n')
    companyName = ' '.join(lines[0].split()[3:])
    stockExchange = ''.join(lines[1].split()[0]).split(':')[0]
    tickerSymbol = ''.join(lines[1].split()[1:])
    price = lines[2].split()[0]
    currency = lines[2].split()[1]
    priceChange = ''.join(lines[2].split()[2][1:])
    percentPriceChange = ''.join(lines[2].split()[3][1:-2])
    
    #Return statement reflecting findings
    return (companyName + ' from the ' + stockExchange + ' is up ' + priceChange + ' ' + 
      currency + ' with a total price of ' + price + ' ' + currency)

if __name__ == '__main__':
    for stock in stocks:
        print(getStockInfo(stock))
