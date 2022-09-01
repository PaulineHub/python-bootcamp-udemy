import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "11PNPIZM345J5JMI"
NEWS_API_KEY = "d1500c9f80cc436fa97631d038daa17b"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": STOCK_API_KEY
}

response = requests.get(
    url=STOCK_ENDPOINT, 
    params=stock_parameters)

response.raise_for_status()
stock_data = response.json()

#print(data)

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
#TODO 2. - Get the day before yesterday's closing stock price

today = datetime.today()
today_day = today.strftime("%Y-%m-%d")
yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")
two_days_ago = (today - timedelta(days=2)).strftime("%Y-%m-%d")

yesterday_stock_price = stock_data['Time Series (Daily)'][yesterday]['4. close']
two_days_ago_stock_price = stock_data['Time Series (Daily)'][two_days_ago]['4. close']


#TODO 3. - Find the positive difference between 1 and 2.
# The abs() function returns the absolute value of the specified number.
stock_price_difference = abs(float(yesterday_stock_price) - float(two_days_ago_stock_price))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (stock_price_difference / float(yesterday_stock_price)) * 100

## STEP 2: https://newsapi.org/
#If TODO4 percentage is greater than 5 then actually get the first 3 news pieces for the COMPANY_NAME..
if diff_percent > 0.5:
    news_parameters = {
        "q": COMPANY_NAME,
        "from": today_day,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(
        url=NEWS_ENDPOINT,
        params=news_parameters)

    response.raise_for_status()
    news_data = response.json()
    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_first_articles = news_data['articles'][:4]
    #print(news_data['articles'][:4])
    articles_list = [{'title': article['title'],
                      'description': article['description']} 
                      for article in three_first_articles]
    print(articles_list)





#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
