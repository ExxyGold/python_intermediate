import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
api_key = "N4R7VGX8BGG04LGF"
parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize":"compact",
    "apikey": api_key
    }

response = requests.get(url = "https://www.alphavantage.co/query", params= parameter)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]

today = dt.datetime.now()

yesterday = today - dt.timedelta(days= 1 )
yesterday_date = yesterday.date()

two_days_ago = today - dt.timedelta(days= 2 )
two_days_ago_date = two_days_ago.date()

yesterday_price = float(stock_data[str(yesterday_date)]["4. close"])
other_price = float(stock_data[str(two_days_ago_date)]["4. close"])

percentage = (yesterday_price - other_price) * 100/ other_price

percentage = round(percentage, 2)


percent_note = ""


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    news_api = "80386e8a341348c5bd77b6d7b3f15c0d"
    news_parameter = {
        "q": COMPANY_NAME,
        "from": f"{yesterday_date}",
        "sortBy": " popularity",
        "apiKey": news_api
    }

    news_response = requests.get(url = "https://newsapi.org/v2/everything", params= news_parameter)
    print(news_response.status_code)
    news_list = news_response.json()["articles"]

    news = {}

    for n in range(3):
        article = news_list[n]
        news[article["title"]] = article["description"]

    return news



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message():
    acct_sid = os.getenv("ACC_SID")
    auth = os.getenv("AUTH_TOKEN")

    client = Client(acct_sid, auth)

    update = get_news()

    for news in update:
        message = client.messages.create(
            body= f"{STOCK}: {percent_note} \n\n Headline: {news}\n\n Brief: {update[news]}",
            from_="whatsapp:+14155238886",
            to="whatsapp:+2348136552264",
            )

    print(message.status)

if percentage >= 5:
    percent_note = f"✅ {percentage}%"
    send_message()
elif percentage <= -5:
    percent_note = f"🔻 {percentage}%"
    send_message()

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

