from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
MAIL = "uuluyol0@gmail.com"
PASSWORD = "gaotmxrlplprrktn"
url = "https://www.amazon.com/Pioneer-DJ-Smart-Controller-DDJ-200/dp/B07RPW4PSS/ref=sr_1_2?crid=2DTSTCZ4TGD7I&keywords=Pioneer+DJ+DDJ-400&qid=1669725519&sprefix=pioneer+dj+ddj-400%2Caps%2C503&sr=8-2"
header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
    # print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole").get_text()
actual_price = price.split(".")[0]
price_as_float = float(actual_price)
print(price_as_float)


title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 100

if price_as_float <= BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MAIL, PASSWORD)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=MAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )



