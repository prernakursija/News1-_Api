import requests #pip insatll requests

query= input("What type of news are you interested in today?:")
api="98a21d3470fd45df8f14b9dfedb5aa3c"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-09-07&sortBy=publishedAt&apiKey={api}"
print(url)
r=requests.get(url)
data= r.json()
articles=data["articles"]
for  index,article in enumerate(articles):
    print(index+1,article["title"], article["url"])
    print("\n************************************\n")