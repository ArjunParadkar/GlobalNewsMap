from newsapi import NewsApiClient
print("Welcome to Global News Map 🌍")
newsapi = NewsApiClient(api_key= "Enter API Key Here")
top_headlines = newsapi.get_top_headlines(country='us')
print(top_headlines)
